from win0 import Ui_win0
from new_graph_win import Ui_new_graph_win
from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure
from ConfigurateWorkspace import Ui_ConfigurateWorkspace
from ImportCsv import Ui_ImportCsv
import pandas as pd
import os
import pickle
import datetime as dt
from warning_msg_replace_label import Ui_warning_msg_replace_label

class Workspace:
    def __init__(self, name):
        self.name = name

    def setDateFrom(self, date):
        pass

    def setDateTo(self, date):
        pass

class WorkspaceCsv(Workspace):
    def __init__(self, name, directory):
        super().__init__(name)
        self.directory = directory.replace("/", "\\") # Not contains the name of the file, only the path
        self.sep = ";"
        self.dataset = None
        self.path_csv = self.directory + "\\" + self.name + ".csv"

        # self.details_labels_show = []
        self.visible_activities_labels = []
        self.hidden_activities_labels = []
        self.visible_involved_people_labels = []
        self.hidden_involved_people_labels = []
        self.selected_date_option = "Last year"
        self.initial_date = dt.date(2000, 1, 1)
        self.final_date = dt.date(2000, 1, 1)

    def loadDataset(self):
        # Load dataset from csv file
        if os.path.exists(self.path_csv) == False:
            file = open(self.path_csv, "w")
            file.write("Date" + self.sep + "Activity" + self.sep + "Details" + self.sep + "Time" + self.sep + "Involved People")
            file.close()

        # ------------------------------------------------- Load dataframe with csv data and configurate it
        self.dataset = pd.read_csv(self.path_csv, sep = ";")

        if len(self.dataset) > 0: # If there are one record at least
            self.dataset[["Date"]] = self.dataset[["Date"]].apply(pd.to_datetime)
            self.dataset["Date"] = self.dataset["Date"].dt.date
            self.dataset = self.dataset.sort_values("Date")

    def setData(self, dataset): # Change name to "setDataStored"
        self.dataset = dataset
        # if os.path.exists(self.path_csv): # Verifiy if exists path_csv and if so remove it
        #     os.remove(self.path_csv)
        # print("setData -------------------------------------------------------")
        # print(self.dataset)
        self.dataset.to_csv(self.path_csv, sep = ";")

    def setSelectedDate(self, option = "Last year", parent = None):
        self.selected_date_option = option
        self.loadDataset() # Load dataset from csv file

        if len(self.dataset) > 0:
            if self.selected_date_option != "Custom period":
                if self.selected_date_option == "Last month":
                    parent.setEnabledSelectionCalendarButtons(False)
                    included = self.dataset["Date"].map(lambda x: x.month) == dt.date.today().month

                elif self.selected_date_option == "Last year":
                    parent.setEnabledSelectionCalendarButtons(False)
                    included = self.dataset["Date"].map(lambda x: x.year) == 2020 # 2020 for test because I don't have a prepared dataset with more years

                elif self.selected_date_option == "Entire history":
                    parent.setEnabledSelectionCalendarButtons(False)
                    included = self.dataset["Date"].map(lambda x: x == x)

                if len(self.dataset[included]) > 0: # "included" is the selected data in previous ifs
                    self.initial_date = self.dataset[included].values[0][0]
                    self.final_date = self.dataset[included].values[len(self.dataset[included]) - 1][0]
            else:
                parent.setEnabledSelectionCalendarButtons(True)
                included = self.dataset["Date"].map(lambda x: self.initial_date <= x <= self.final_date)
            print("    len(dataset[included]): ", len(self.dataset[included]))
            self.dataset = self.dataset[included]
            self.dataset.index = pd.RangeIndex(0, len(self.dataset))

            # ---------------------------------------------------------------------------- Set previously labels activities
            hidden_activities = self.hidden_activities_labels
            hidden_people = self.hidden_involved_people_labels
            self.setActivitiesLabels()
            self.setInvolvedPeopleLabels()

            for label in self.visible_activities_labels:
                if label in hidden_activities:
                    self.visible_activities_labels.remove(label)

            for label in self.visible_involved_people_labels:
                if label in hidden_people:
                    self.visible_involved_people_labels.remove(label)
            self.filterPeopleLabels()
            self.filterActivitiesLabels()

    def setActivitiesLabels(self):
        # By default all activities labels are stored in activity_labels_show list
        self.visible_activities_labels = []
        for i in self.dataset.loc[:, "Activity"]:
            if str(i) != "nan":
                record_labels = str(i).split(",")
                for label in record_labels:
                    if label not in self.visible_activities_labels:
                        self.visible_activities_labels.append(label)
        self.visible_activities_labels.sort()

    def setInvolvedPeopleLabels(self):
        # By default all people labels are stored in involved_people_labels_show list
        self.visible_involved_people_labels = []
        for i in self.dataset.loc[:, "Involved People"]:
            if str(i) != "nan":
                record_labels = str(i).split(",")
                for label in record_labels:
                    if label not in self.visible_involved_people_labels:
                        self.visible_involved_people_labels.append(label)
        self.visible_involved_people_labels.sort()

    def labelInList(self, string, label_list):
        # Detect if a substring comma separated in list and returns True
        if str(string) != "nan":
            for s in string.split(","):
                if s in label_list:
                    return True # If data it's in label list
            return False # If data it's not in label_list
        else:
            return False # If data is nan

    def filterActivitiesLabels(self):
        # If records which contains the activities labels that are hidden it will be removed of the dataframe to show
        if len(self.hidden_activities_labels) > 0:
            for i, string in enumerate(self.dataset.loc[:, "Activity"]):
                if self.labelInList(string, self.hidden_activities_labels):
                    self.dataset.drop([i], axis = 0, inplace = True)
            self.dataset.index = pd.RangeIndex(0, len(self.dataset))

    def filterPeopleLabels(self):
        if len(self.hidden_involved_people_labels) > 0:
            for i, string in enumerate(self.dataset.loc[:, "Involved People"]):
                if self.labelInList(string, self.hidden_involved_people_labels):
                    self.dataset.drop([i], axis = 0, inplace = True)
            self.dataset.index = pd.RangeIndex(0, len(self.dataset))

    def removeRecord(self, dataset, index):
        print("removeRecord")
        dataset.drop([index], axis = 0, inplace = True)
        dataset = dataset.reset_index(drop = True)

    def changeActLabel(self, prev_label, new_label):
        # Change the previous label for the new label in the hidden activities
        for i, label in enumerate(self.hidden_activities_labels): 
            if label == prev_label:
                self.hidden_activities_labels[i] = new_label
        
        # Get records from the csv file of the workspace
        dataset = pd.read_csv(self.path_csv, sep = ";")
        for i, string in enumerate(dataset["Activity"]):
            split_string = string.split(",") # Bug because there are a nan string
            new_string = ""
            j = 0
            # If new_label has no any character and if split_string has only 1 element remove the record that contains the modified label
            if len(split_string) == 1 and new_label == "":
                if split_string[0] == prev_label:
                    self.removeRecord(dataset, i)
            else: # If no, iterate on all elements of split_string and replace the string which = prev_label for new_label
                while j < len(split_string) - 1:
                    if split_string[j] == prev_label:
                        if new_label != "": # If label was not deleted
                            new_string += new_label + ","
                    else:
                        new_string += split_string[j] + ","
                    j += 1
                # ----------------------------------------------------- In last label comma is not write
                if split_string[len(split_string) - 1] == prev_label:
                    new_string += new_label
                else:
                    new_string += split_string[len(split_string) - 1]
                dataset.loc[i, "Activity"] = new_string # Add the modified string to the dataframe
        dataset["Date"] = pd.to_datetime(dataset["Date"], format = "%Y-%m-%d") # Convert data from "Date" column to datetime type 
        dataset = dataset.set_index("Date") # Set the column "Date" as index. This avoids that a new column with int values has be added
        dataset.to_csv(self.path_csv, sep = ";")

    def changePeopleLabel(self, prev_label, new_label):
        for i, label in enumerate(self.hidden_involved_people_labels):
            if label == prev_label:
                self.hidden_involved_people_labels[i] = new_label
        dataset = pd.read_csv(self.path_csv, sep = ";")
        for i, string in enumerate(dataset["Involved People"]):
            if str(string) != "nan":
                split_string = string.split(",")
                new_string = ""
                j = 0
                while j < len(split_string) - 1:
                    if split_string[j] == prev_label:
                        new_string += new_label + ","
                    else:
                        new_string += split_string[j] + ","
                    j += 1
                # ----------------------------------------------------- In last label comma is not write
                if split_string[len(split_string) - 1] == prev_label:
                    new_string += new_label
                else:
                    new_string += split_string[len(split_string) - 1]
                dataset.loc[i, "Involved People"] = new_string
        dataset["Date"] = pd.to_datetime(dataset["Date"], format = "%Y-%m-%d")
        dataset = dataset.set_index("Date")
        dataset.to_csv(self.path_csv, sep = ";")

# ------------------------------------------------------------------------------------------------------------------------------------------------------------
class ConfigurateWorkspace(QtWidgets.QDialog, Ui_ConfigurateWorkspace):
    def __init__(self, parent = None):
        self.parent = parent
        super().__init__(self.parent)
        self.setupUi(self)
        self.checkbox_csv.clicked.connect(self.csvClicked)
        self.checkbox_database.clicked.connect(self.databaseClicked)
        self.examin_button.clicked.connect(self.selectCsvDirectory)

    def csvClicked(self):
        if self.checkbox_csv.checkState() == 2:
            if self.checkbox_database.checkState() == 2:
                self.checkbox_database.setCheckState(0)
                self.activateDatabaseWorkspace(False)
            self.activateCsvWorkspace()
        elif self.checkbox_csv.checkState() == 0:
            self.activateCsvWorkspace(False)

    def databaseClicked(self):
        if self.checkbox_database.checkState() == 2:
            if self.checkbox_csv.checkState() == 2:
                self.checkbox_csv.setCheckState(0)
                self.activateCsvWorkspace(False)
            self.activateDatabaseWorkspace()
        elif self.checkbox_database.checkState() == 0:
            self.activateDatabaseWorkspace(False)

    def activateCsvWorkspace(self, state=True):
        self.lineedit_csv.setEnabled(state)
        self.examin_button.setEnabled(state)

    def activateDatabaseWorkspace(self, state=True):
        self.lineedit_db_name.setEnabled(state)
        self.lineedit_pass.setEnabled(state)
        self.lineedit_service.setEnabled(state)
        self.lineedit_table_name.setEnabled(state)
        self.lineedit_user.setEnabled(state)

    def accept(self):
        # ----------------------------------------- Set csv workspace
        if self.checkbox_csv.checkState() == 2:
            directory = self.lineedit_csv.text()
            name = self.lineedit_workspace_name.text()
            workspace = WorkspaceCsv(name, directory)
            file = open(directory + "\\" + name + ".works", "wb")
            pickle.dump(workspace, file)
            file.close()
            self.parent.loadWorkspace(workspace)
        else:
            # ---------------------------------------- Set database workspace
            print("database workspace not developed yet")

        # ---------------------------------------- Destroy QDialog
        self.destroy()

    def reject(self):
        print("Reject")
        self.destroy()

    def selectCsvDirectory(self):
        directory_path = QtWidgets.QFileDialog.getExistingDirectory(self, "Select directory")
        print(directory_path)
        self.lineedit_csv.setText(directory_path)

#------------------------------------------------------------------------------------------------------------------------------------------------------------
class Canvas:
    def __init__(self):
        self.fig = Figure((130, 6), dpi = 70)
        self.canvas = FigureCanvas(self.fig)
        self.graph = self.fig.add_subplot(111)

#------------------------------------------------------------------------------------------------------------------------------------------------------------
class LinearGraph(Canvas):
    def __init__(self):
        super().__init__()
        # ------------------------------------------- Example data
        x_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        y_data = [12, 45, 78, 34, 56, 78, 12, 23, 37, 40]
        self.graph.plot(x_data, y_data)

#------------------------------------------------------------------------------------------------------------------------------------------------------------
class NewGraphWin(QtWidgets.QDialog, Ui_new_graph_win):
    parent = None
    def __init__(self, parent=None):
        self.parent = parent
        super().__init__(self.parent)
        self.setupUi(self)
        self.combo_box_graph_types.addItem("Linear Graph")

    def reject(self):
        self.destroy()

    def accept(self):
        self.parent.createLinearGraph()
        self.destroy()

# -------------------------------------------------------------------------------
class ImportCsv(QtWidgets.QDialog, Ui_ImportCsv):
    def __init__(self, parent=None):
        self.parent = parent
        self.fields_list = []
        self.normalized_fields_names = ["Date", "Activity", "Details", "Time", "Involved People"]
        super().__init__(self.parent)
        self.setupUi(self)
        self.import_button.clicked.connect(self.openCsv)
        self.lineedit_directory.setEnabled(False) # Entry box of the csv directory it's disable until click on "Examin" button
        self.directory = ""
        self.imported_dataset = None
        self.normalized_dataset = None

    def openCsv(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, "Select Csv")
        self.lineedit_directory.setText(fname[0])
        self.directory = fname[0].replace("/", "\\")
        self.imported_dataset = pd.read_csv(self.directory, sep = ";")
        self.comboBox_date.addItems(self.imported_dataset.columns)
        self.comboBox_activity.addItems(self.imported_dataset.columns)
        self.comboBox_details.addItems(self.imported_dataset.columns)
        self.comboBox_time.addItems(self.imported_dataset.columns)
        self.comboBox_involved_people.addItems(self.imported_dataset.columns)

    def gatherFields(self):
        self.fields_list = []
        self.fields_list.append(self.comboBox_date.currentText())
        self.fields_list.append(self.comboBox_activity.currentText())
        self.fields_list.append(self.comboBox_details.currentText())
        self.fields_list.append(self.comboBox_time.currentText())
        self.fields_list.append(self.comboBox_involved_people.currentText())

    def validate_duplicates_combobox(self):
        # If there are one field of the csv file for more than one field of the workspace returns true, else false
        for i in range(5):
            if self.fields_list.count(self.fields_list[i]) > 1:
                return True
        return False

    def accept(self):
        self.gatherFields()
        if self.validate_duplicates_combobox():
            msg = QtWidgets.QMessageBox(self)
            msg.setWindowTitle("Duplicates fields")
            msg.setText("There are duplicates fields")
            msg.exec_()
        else:
            self.normalized_dataset = self.imported_dataset[[self.fields_list[i] for i in range(len(self.fields_list))]]
            self.normalized_dataset.columns = self.normalized_fields_names
            self.normalized_dataset["Date"] = pd.to_datetime(self.normalized_dataset["Date"], format = "%d/%m/%Y", errors = "coerce")
            self.normalized_dataset = self.normalized_dataset.set_index("Date")

            self.parent.workspace.setData(self.normalized_dataset)
            self.parent.workspace.loadDataset()
            self.parent.workspace.setSelectedDate(parent = self.parent)
            self.parent.loadTable(self.parent.workspace.dataset)
            self.destroy()

    def reject(self):
        self.destroy()

class WarningMsgReplaceLabel(QtWidgets.QDialog, Ui_warning_msg_replace_label):
    def __init__(self, name_model_list, prev_label = "", new_label = "", parent = None):
        self.parent = parent
        super().__init__(self.parent)
        self.setupUi(self)
        self.prev_label = prev_label
        self.new_label = new_label
        self.setLabelsToReplace()
        self.name_model_list = name_model_list # Name of the list the label is in
        
    def accept(self):
        if self.name_model_list == "item_model_visible_acts" or self.name_model_list == "item_model_hidden_acts":
            self.parent.actsItemChanged(self.prev_label, self.new_label)
        elif self.name_model_list == "item_model_visible_people" or self.name_model_list == "item_model_hidden_people":
            self.parent.peopleItemChanged(self.prev_label, self.new_label)
        self.destroy()

    def reject(self):
        self.destroy()

    def setLabelsToReplace(self, prev_label = None, new_label = None):
        if prev_label != None:
            self.prev_label = prev_label
        if new_label != None:
            self.new_label = new_label
        string = 'Are you sure you want replace all "' + self.prev_label + '" labels by "' + self.new_label + '"?'
        font = QtGui.QFont()
        font.setPixelSize(13)
        self.label_warning_replace = QtWidgets.QLabel(self)
        self.label_warning_replace.setFont(font)
        string_width = self.label_warning_replace.fontMetrics().boundingRect(string).width()
        self.label_warning_replace.setText(string)
        self.label_warning_replace.setMinimumWidth(string_width)
        self.setMinimumWidth(string_width + 20)
        self.label_warning_replace.move(10, 5)
        self.label_warning_replace.show()

        # self.label = QtWidgets.QLabel('Are you sure you want replace "' + prev_label + '" by "' + new_label + '" in all records?')
        # self.label = QtWidgets.QLabel(self)
        # self.label.setText("Hello")
        # self.label.
        # self.
# --------------------------------------------------------------------------------------------------------------------------------------------------------
class Win0(QtWidgets.QMainWindow, Ui_win0):
    def __init__(self):
        super().__init__()
        self.selected_date_options = ["Last year", "Last month", "Entire history", "Custom period"]

        self.setupUi(self)
        # ---------------------------------------------------------- Set the configuration of the tabs
        self.tabs.tabBarClicked.connect(self.newTab)
        self.setClosableTabs()
        self.tabs.tabCloseRequested.connect(self.closeTab)

        self.current_item_selected = "" # When an item it's selected in a QListView widget

        # ---------------------------------------------------------- Instance attributes
        self.graph_layouts_list = [] # Stores the layouts which contains
        self.calendar = None
        self.calendar_btn = None
        self.dataset = None
        self.workspace = None
        self.item_model_hidden_acts = QtGui.QStandardItemModel()
        self.item_model_visible_acts = QtGui.QStandardItemModel()
        self.item_model_hidden_people = QtGui.QStandardItemModel()
        self.item_model_visible_people = QtGui.QStandardItemModel()
        # self.flag_want_replace_label = False # Flag for confirm user wants to replace a label for other

        # ---------------------------------------------------------- Store layouts of the tabs that contains the graphs
        self.graph_layouts_list.append(None)
        self.graph_layouts_list.append(self.graph_layout)


        # ----------------------------------------------------------- Set calendar buttons function
        self.button_date_from.clicked.connect(self.showCalendar)
        self.button_date_to.clicked.connect(self.showCalendar)
        self.button_date_selected.clicked.connect(self.showCalendar)

        # ----------------------------------------------------------- Set the Event Filter for the widgets

        # ------------------------------------ Section "Configurate Selection"
        self.combo_box_ops_date.installEventFilter(self)
        self.combo_box_ops_time.installEventFilter(self)
        self.date_from.installEventFilter(self)
        self.date_to.installEventFilter(self)

        # Lists ------------------------------
        self.hidden_acts_list.installEventFilter(self)
        self.visible_acts_list.installEventFilter(self)
        self.hidden_people_list.installEventFilter(self)
        self.visible_people_list.installEventFilter(self)

        # Buttons ----------------------------
        self.button_visible_all_acts.installEventFilter(self)
        self.button_hide_all_acts.installEventFilter(self)
        self.button_visible_act.installEventFilter(self)
        self.button_hide_act.installEventFilter(self)
        self.button_visible_all_people.installEventFilter(self)
        self.button_hide_all_people.installEventFilter(self)
        self.button_hide_people.installEventFilter(self)
        self.button_visible_people.installEventFilter(self)

        # self.button_hide_act.clicked.connect(self.hideAct())

        # Time -----------------------------
        self.spin_hours_2.installEventFilter(self)
        self.spin_min_2.installEventFilter(self)
        self.spin_sec_2.installEventFilter(self)
        self.spin_hours_3.installEventFilter(self)
        self.spin_min_3.installEventFilter(self)
        self.spin_sec_3.installEventFilter(self)
        self.default_button.installEventFilter(self)

        # ------------------------------------ Section "Manage Register"
        self.date_selected.installEventFilter(self)
        self.spin_hours.installEventFilter(self)
        self.spin_min.installEventFilter(self)
        self.spin_sec.installEventFilter(self)
        self.activities_list.installEventFilter(self)
        self.details_list.installEventFilter(self)
        self.involved_people_list.installEventFilter(self)
        self.activity_line_edit.installEventFilter(self)
        self.details_line_edit.installEventFilter(self)
        self.involved_people_line_edit.installEventFilter(self)
        self.add_activity_button.installEventFilter(self)
        self.update_activity_button.installEventFilter(self)
        self.remove_activity_button.installEventFilter(self)
        self.add_details_button.installEventFilter(self)
        self.update_details_button.installEventFilter(self)
        self.remove_details_button.installEventFilter(self)
        self.add_involved_people_button.installEventFilter(self)
        self.update_involved_people_button.installEventFilter(self)
        self.remove_involved_people_button.installEventFilter(self)
        
        self.new_button.installEventFilter(self)
        self.update_button.installEventFilter(self)
        self.unselect_button.installEventFilter(self)
        self.delete_button.installEventFilter(self)

        # ------------------------------------ Other sections
        self.table1.installEventFilter(self)
        self.menubar.installEventFilter(self)

        # ----------------------------------------------------- Set menu bar functions
        self.new_workspace_menu.triggered.connect(self.newWorkspace)
        self.import_menu.triggered.connect(self.importCsv)

        # ----------------------------------------------------- Others
        self.setEnabledWidgets(False)
        self.combo_box_ops_date.addItems(self.selected_date_options)
        self.loadLastWorkspace()
        self.setEnabledSelectionCalendarButtons(False)

        # ----------------------------------------------------- Set the list's models
        self.item_model_hidden_acts.setObjectName("item_model_hidden_acts")
        self.item_model_visible_acts.setObjectName("item_model_visible_acts")
        self.item_model_hidden_people.setObjectName("item_model_hidden_people")
        self.item_model_visible_people.setObjectName("item_model_visible_people")

        self.visible_acts_list.setModel(self.item_model_visible_acts)
        self.visible_people_list.setModel(self.item_model_visible_people)
        self.hidden_acts_list.setModel(self.item_model_hidden_acts)
        self.hidden_people_list.setModel(self.item_model_hidden_people)

        # self.item_model_visible_acts.itemChanged.connect(self.actsItemChanged)
        # self.item_model_visible_people.itemChanged.connect(self.peopleItemChanged)
        # self.item_model_hidden_acts.itemChanged.connect(self.actsItemChanged)
        # self.item_model_hidden_people.itemChanged.connect(self.peopleItemChanged)

        self.item_model_visible_acts.itemChanged.connect(self.showWarningMsgReplaceLabel)
        self.item_model_visible_people.itemChanged.connect(self.showWarningMsgReplaceLabel)
        self.item_model_hidden_acts.itemChanged.connect(self.showWarningMsgReplaceLabel)
        self.item_model_hidden_people.itemChanged.connect(self.showWarningMsgReplaceLabel)

        # --------------------------------------------------- Set activity and people labels filters functionality
        for button in [self.button_hide_act, self.button_visible_act, self.button_visible_people, self.button_hide_people]:
            button.setEnabled(False)

        self.button_hide_act.clicked.connect(self.hideAct)
        self.button_visible_act.clicked.connect(self.visibleAct)
        self.button_hide_people.clicked.connect(self.hidePeople)
        self.button_visible_people.clicked.connect(self.visiblePeople)

        self.visible_acts_list.selectionModel().selectionChanged.connect(self.itemSelectedVisibleActs)
        self.visible_people_list.selectionModel().selectionChanged.connect(self.itemSelectedVisibilePeople)
        self.hidden_acts_list.selectionModel().selectionChanged.connect(self.itemSelectedHiddenActs)
        self.hidden_people_list.selectionModel().selectionChanged.connect(self.itemSelectedHiddenPeople)

    def actsItemChanged(self, prev_label, new_label = ""):
    # def actsItemChanged(self, item):
        # It take the previously item selected and change it for the new item
        self.workspace.changeActLabel(prev_label, new_label)
        self.workspace.setSelectedDate(self.workspace.selected_date_option, self) # Bug when window is closed after change a label TC10.2
        self.loadTable(self.workspace.dataset)
        self.current_item_selected = ""

    def peopleItemChanged(self, prev_label, new_label):
        self.workspace.changePeopleLabel(prev_label, new_label)
        self.workspace.setSelectedDate(self.workspace.selected_date_option, self)
        self.loadTable(self.workspace.dataset)
        self.current_item_selected = ""

    # def showWarningMsgReplaceLabel(self, prev_label, new_label):
    def showWarningMsgReplaceLabel(self, item):
        # Bug: When a label is changed and we want change other of the same list the function "showWarningMsgReplaceLabel" not works
        prev_label = self.current_item_selected
        new_label = item.text()
        warning_msg = WarningMsgReplaceLabel(item.model().objectName(), prev_label, new_label, self)
        warning_msg.show()

    def hideAct(self):
        for index in self.visible_acts_list.selectedIndexes(): # This loop has a bug
            print("for hideAct")
            item = self.visible_acts_list.model().itemFromIndex(index)
            self.hidden_acts_list.model().appendRow(QtGui.QStandardItem(item.text()))
            self.workspace.visible_activities_labels.remove(item.text())
            self.workspace.hidden_activities_labels.append(item.text())
            self.visible_acts_list.model().removeRow(item.row())
        print("hideAct")
        self.visible_acts_list.selectionModel().clearSelection() # Here it's the bug, it's triggering some event which calls eventFilter
        self.workspace.filterActivitiesLabels()
        self.loadTable(self.workspace.dataset)

    def visibleAct(self):
        for index in self.hidden_acts_list.selectedIndexes():
            item = self.hidden_acts_list.model().itemFromIndex(index)
            self.visible_acts_list.model().appendRow(QtGui.QStandardItem(item.text()))
            self.workspace.hidden_activities_labels.remove(item.text())
            self.workspace.visible_activities_labels.append(item.text())
            self.hidden_acts_list.model().removeRow(item.row())
        self.hidden_acts_list.selectionModel().clearSelection()
        self.workspace.setActivitiesLabels()
        self.workspace.filterActivitiesLabels()
        self.workspace.setSelectedDate(self.workspace.selected_date_option, self)
        self.loadTable(self.workspace.dataset)

    def hidePeople(self):
        for index in self.visible_people_list.selectedIndexes():
            item = self.visible_people_list.model().itemFromIndex(index)
            self.hidden_people_list.model().appendRow(QtGui.QStandardItem(item.text()))
            self.workspace.visible_involved_people_labels.remove(item.text())
            self.workspace.hidden_involved_people_labels.append(item.text())
            self.visible_people_list.model().removeRow(item.row())
        self.visible_people_list.selectionModel().clearSelection()
        self.workspace.filterPeopleLabels()
        self.loadTable(self.workspace.dataset)

    def visiblePeople(self):
        for index in self.hidden_people_list.selectedIndexes():
            item = self.hidden_people_list.model().itemFromIndex(index)
            self.visible_people_list.model().appendRow(QtGui.QStandardItem(item.text()))
            self.workspace.hidden_involved_people_labels.remove(item.text())
            self.workspace.visible_involved_people_labels.append(item.text())
            self.hidden_people_list.model().removeRow(item.row())
        self.hidden_people_list.selectionModel().clearSelection()
        self.workspace.setInvolvedPeopleLabels()
        self.workspace.filterPeopleLabels()
        self.workspace.setSelectedDate(self.workspace.selected_date_option, self)
        self.loadTable(self.workspace.dataset)

    def hideAllActs(self):
        pass

    def visibleAllActs(self):
        pass

    def hideAllPeople(self):
        pass

    def visibleAllPeople(self):
        pass

    def itemSelectedVisibleActs(self):
        # print("itemSelectedVisibleActs")
        selected_indexes = self.visible_acts_list.selectedIndexes()
        self.button_hide_act.setEnabled(bool(selected_indexes))
        self.button_visible_act.setEnabled(False)
        self.button_visible_people.setEnabled(False)
        self.button_hide_people.setEnabled(False)
        if len(self.visible_acts_list.selectedIndexes()) > 0:
            for index in self.visible_acts_list.selectedIndexes():
                self.current_item_selected = self.visible_acts_list.model().itemFromIndex(index).text()
                break

    def itemSelectedHiddenActs(self):
        self.button_visible_act.setEnabled(bool(self.hidden_acts_list.selectedIndexes()))
        self.button_hide_act.setEnabled(False)
        self.button_visible_people.setEnabled(False)
        self.button_hide_people.setEnabled(False)
        if len(self.hidden_acts_list.selectedIndexes()) > 0:
            for index in self.hidden_acts_list.selectedIndexes():
                self.current_item_selected = self.hidden_acts_list.model().itemFromIndex(index).text()
                break

    def itemSelectedVisibilePeople(self):
        self.button_hide_people.setEnabled(bool(self.visible_people_list.selectedIndexes()))
        self.button_visible_people.setEnabled(False)
        self.button_visible_act.setEnabled(False)
        self.button_hide_act.setEnabled(False)
        if len(self.visible_people_list.selectedIndexes()) > 0:
            for index in self.visible_people_list.selectedIndexes():
                self.current_item_selected = self.visible_people_list.model().itemFromIndex(index).text()
                break

    def itemSelectedHiddenPeople(self):
        self.button_visible_people.setEnabled(bool(self.hidden_people_list.selectedIndexes()))
        self.button_hide_people.setEnabled(False)
        self.button_visible_act.setEnabled(False)
        self.button_hide_act.setEnabled(False)
        if len(self.hidden_people_list.selectedIndexes()) > 0:
            for index in self.hidden_people_list.selectedIndexes():
                self.current_item_selected = self.hidden_people_list.model().itemFromIndex(index).text()
                break

    def setEnabledSelectionCalendarButtons(self, state = True):
        self.button_date_from.setEnabled(state)
        self.button_date_to.setEnabled(state)

    def setEnabledWidgets(self, state = True):
        self.tabs.setEnabled(state)
        self.import_menu.setEnabled(state)
        self.save_workspace_menu.setEnabled(state)
        self.saveas_workspace_menu.setEnabled(state)

    def loadWorkspace(self, workspace):
        # print("loadworkspace")
        self.workspace = workspace
        self.workspace.loadDataset()
        if len(self.workspace.dataset) > 0: #If the dataset get at least 1 record
            self.workspace.setSelectedDate(self.workspace.selected_date_option, self)
            self.loadTable(self.workspace.dataset)
        self.setEnabledWidgets(True)

    def loadTable(self, dataset):
        # print("loadTable")
        rows_num = len(dataset)
        cols_num = self.table1.columnCount()
        values = dataset.values

        if rows_num > 100: # If there are more rows than 100 (default number)
            self.table1.setRowCount(rows_num)
        elif rows_num < 100:
            self.table1.setRowCount(100)

        if rows_num < self.table1.rowCount(): # If new records are less than previous records in the table then clean the table
            difference = self.table1.rowCount() - rows_num
            for i in range(rows_num, rows_num + difference):
                for j in range(cols_num):
                    self.table1.setItem(i, j, QtWidgets.QTableWidgetItem(""))

        for i in range(rows_num):
            for j in range(cols_num):
                self.table1.setItem(i, j, QtWidgets.QTableWidgetItem(str(values[i][j])))

        # -------------------------------------------------------------- Set date in the QDateEdit widgets
        d1 = self.workspace.initial_date
        d2 = self.workspace.final_date
        self.date_from.setDate(QtCore.QDate(d1.year, d1.month, d1.day))
        self.date_to.setDate(QtCore.QDate(d2.year, d2.month, d2.day))

        # self.workspace.setAllInvolvedPeopleLabels() # codigo sospechoso
        self.loadVisibleActsTable()
        self.loadVisibleInvolvedPeopleTable()
        self.loadHiddenActsTable()
        self.loadHiddenInvolvedPeopleTable()

    def loadVisibleActsTable(self): # Load all activities labels table
        self.item_model_visible_acts.clear()
        for i in self.workspace.visible_activities_labels:
            item = QtGui.QStandardItem(i)
            self.item_model_visible_acts.appendRow(item)

    def loadHiddenActsTable(self):
        self.item_model_hidden_acts.clear()
        for i in self.workspace.hidden_activities_labels:
            item = QtGui.QStandardItem(i)
            self.item_model_hidden_acts.appendRow(item)

    def loadVisibleInvolvedPeopleTable(self):
        self.item_model_visible_people.clear()
        for i in self.workspace.visible_involved_people_labels:
            item = QtGui.QStandardItem(i)
            self.item_model_visible_people.appendRow(item)

    def loadHiddenInvolvedPeopleTable(self):
        self.item_model_hidden_people.clear()
        for i in self.workspace.hidden_involved_people_labels:
            item = QtGui.QStandardItem(i)
            self.item_model_hidden_people.appendRow(item)

    def loadLastWorkspace(self):
        if os.path.exists("last.txt"):
            last_file = open("last.txt", "r")
            file_path = last_file.read()
            if os.path.exists(file_path + ".works"): # If exists .works file
                file = open(file_path + ".works", "rb")
                self.workspace = pickle.load(file)
                file.close()
                self.setEnabledWidgets(True)
                self.loadWorkspace(self.workspace)

    def importCsv(self):
        import_csv = ImportCsv(self)
        # import_csv.exec_()
        import_csv.show()

    def eventFilter(self, obj, event):
        # print("event: ", event, " | obj: ", obj)
        if self.workspace != None:
            if event.type() == QtCore.QEvent.FocusIn: # If focus in widget
                self.mousePressEvent(event)
                if type(obj) == type(QtWidgets.QPushButton()): # If button it's one of the label filters
                    btn_name = obj.objectName()
                    if btn_name == "button_hide_act":
                        # print("hide_act")
                        self.hideAct()
                    elif btn_name == "button_visible_act":
                        self.visibleAct()
                    elif btn_name == "button_hide_people":
                        self.hidePeople()
                    elif btn_name == "button_visible_people":
                        self.visiblePeople()
                else: # If it's not a button
                    self.unselectListViewItems(obj)

            elif type(obj) == type(QtWidgets.QListView()):
            # elif type(obj) == type(QtWidgets.QListView()) or type(obj) == type(QtWidgets.QMenuBar()): # If it's list or menubar
                if event.type() == QtCore.QEvent.MouseButtonPress: # If it was clicked
                    self.mousePressEvent(event)

            elif type(obj) == type(QtWidgets.QMenuBar()):
                if event.type() == 2: # MouseButtonPress event
                    self.unselectListViewItems(obj)

            elif type(obj) == type(QtWidgets.QComboBox()): # If type widget it's combo box
                if obj.objectName() == "combo_box_ops_date": # If date selection combo box its clicked
                    if type(event) == QtGui.QPaintEvent:
                        if obj.currentText() != self.workspace.selected_date_option: # If option was changed
                            self.workspace.setSelectedDate(obj.currentText(), self)
                            self.loadTable(self.workspace.dataset)

        return super().eventFilter(obj, event)

    def unselectListViewItems(self, obj):
        if type(obj) != type(QtWidgets.QListView()):
            self.visible_acts_list.selectionModel().clearSelection()
            self.visible_people_list.selectionModel().clearSelection()
            self.hidden_acts_list.selectionModel().clearSelection()
            self.hidden_people_list.selectionModel().clearSelection()
        else:
            for list in [self.visible_people_list, self.visible_acts_list, self.hidden_acts_list, self.hidden_people_list]:
                if obj.objectName() != list.objectName():
                    list.selectionModel().clearSelection()

    def mousePressEvent(self, event):
        # print("mouse pressed: ", event)
        # self.visible_acts_list.clearSelection()
        self.destroyCalendar()

    def newTab(self, event):
        self.destroyCalendar()
        if event == self.tabs.count() - 1:
            new_graph = NewGraphWin(self)
            # new_graph.exec_()
            new_graph.show()

    def setClosableTabs(self):
        self.tabs.setTabsClosable(False)
        self.tabs.setTabsClosable(True)
        self.tabs.tabBar().setTabButton(0, QtWidgets.QTabBar.RightSide, None)
        self.tabs.tabBar().setTabButton(self.tabs.count() - 1, QtWidgets.QTabBar.RightSide, None)

    def closeTab(self, event):
        self.tabs.removeTab(event)
        if self.tabs.count() == 2:
            self.tabs.setCurrentIndex(0)

    def createNewTab(self):

        tab = QtWidgets.QWidget()      

        self.tabs.insertTab(self.tabs.count(), tab, "+")
        self.setClosableTabs()

        # --------------------------------------- Create the vertical layout in which the canvas will be putted
        verticalLayoutWidget = QtWidgets.QWidget(tab)
        verticalLayoutWidget.setGeometry(QtCore.QRect(19, 20, 1060, 630))
        verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        graph_layout = QtWidgets.QVBoxLayout(verticalLayoutWidget)
        graph_layout.setContentsMargins(0, 0, 0, 0)
        graph_layout.setObjectName("graph_layout")

        # --------------------------------------- Add the graph_layout to the list
        graph_layouts_list = self.graph_layouts_list
        graph_layouts_list.append(graph_layout)
        self.graph_layouts_list = graph_layouts_list

    def createLinearGraph(self):
        self.createNewTab()

        # ------------------------------------------------------ Plot and place graph
        linear_graph = LinearGraph()
        self.graph_layouts_list[self.tabs.count() - 2].addWidget(linear_graph.canvas)
        self.tabs.setTabText(self.tabs.count() - 2, "Linear Graph")
        self.tabs.setCurrentIndex(self.tabs.count() - 2)

    def showCalendar(self):
        if self.calendar != None:
            self.destroyCalendar()
        else:
            # ------------------------------------------------------- Get button pressed
            self.calendar_btn = self.sender()
            coordinates = self.calendar_btn.mapTo(self, QtCore.QPoint())

            # ------------------------------------------------------- Place and set calendar
            self.calendar = QtWidgets.QCalendarWidget(self)
            self.calendar.setGeometry(coordinates.x(), coordinates.y() + 20, 280, 200)
            self.calendar.setStyleSheet("background-color: rgb(45, 45, 45);\ncolor: rgb(200, 200, 200);\nalternate-background-color: rgb(85, 85, 127);\ngridline-color: rgb(255, 255, 255);")
            self.calendar.setGridVisible(True)
            self.calendar.setFirstDayOfWeek(QtCore.Qt.Monday)

            # ------------------------------------------------------ Set actual date
            if self.calendar_btn.objectName() == "button_date_from":
                d = self.workspace.initial_date
            elif self.calendar_btn.objectName() == "button_date_to":
                d = self.workspace.final_date
            self.calendar.setSelectedDate(QtCore.QDate(d.year, d.month, d.day))

            self.calendar.show()
            self.calendar.clicked.connect(self.clickCalendar)

    def clickCalendar(self, date):
        btn_name = self.calendar_btn.objectName()

        d = dt.date(date.year(), date.month(), date.day())
        # ------------------------------------------ Set date
        if btn_name != "button_date_selected":
            if btn_name == "button_date_from":
                # For workspace it's used datetime.date type because dataframe works with it
                self.date_from.setDate(date)
                self.workspace.initial_date = d
            elif btn_name == "button_date_to":
                self.date_to.setDate(date)
                self.workspace.final_date = d
            print("Load table")
            self.workspace.setSelectedDate(self.workspace.selected_date_option, self)
            self.loadTable(self.workspace.dataset)

        else:
            self.date_selected.setDate(date)
        self.destroyCalendar()

    def destroyCalendar(self):

        if self.calendar != None:
            self.calendar.hide()
            self.calendar.destroy()
            self.calendar = None

    def newWorkspace(self):
        new_workspace_win = ConfigurateWorkspace(self)
        # new_workspace_win.exec_()
        new_workspace_win.show()

    def saveLastWorkspaceUsed(self):
        file = open("last.txt", "w")
        file.write(self.workspace.directory + "\\" + self.workspace.name)
        file.close()

    def closeEvent(self, event):
        self.saveLastWorkspaceUsed()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Win0()
    ui.show()
    app.setStyle("Fusion")
    sys.exit(app.exec_())





