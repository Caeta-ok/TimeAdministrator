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

        self.activity_labels = []
        self.details_labels = []
        self.involved_people_labels = []

    def loadDataset(self):
        if os.path.exists(self.path_csv):
            file = open(self.path_csv, "r")
        else:
            file = open(self.path_csv, "w")
            file.write("Date" + self.sep + "Activity" + self.sep + "Details" + self.sep + "Time" + self.sep + "Involved Person")
        file.close()
        self.dataset = pd.read_csv(self.path_csv, sep = ";")

    def setData(self, dataset):
        self.dataset = dataset
        self.dataset.to_csv(self.path_csv, sep = ";")
    
    def set_activities_labels(self):
        for i in range(len(self.dataset)):
            record_labels = self.dataset.loc[i, "Activity"].split(",")
            for label in record_labels:
                if label not in self.activity_labels:
                    self.activity_labels.append(label)
        print(self.activity_labels)
# ------------------------------------------------------------------------------------------------------------------------------------------------------------
class ConfigurateWorkspace(QtWidgets.QDialog, Ui_ConfigurateWorkspace):
    parent = None
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
        self.normalized_fields_names = ["Date", "Activity", "Details", "Time", "Involved Persons"]
        super().__init__()
        self.setupUi(self)
        self.import_button.clicked.connect(self.openCsv)
        self.lineedit_directory.setEnabled(False)
        self.directory = ""
        self.imported_dataset = None
        self.normalized_dataset = None

    def openCsv(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, "Select Csv")
        self.lineedit_directory.setText(fname[0])
        self.directory = fname[0].replace("/", "\\")
        self.imported_dataset = pd.read_csv(self.directory, sep = ";", encoding = "utf-8")

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
        # functional requeriment: #4 - 2)
        for i in range(5):
            if self.fields_list.count(self.fields_list[i]) > 1:
                print(self.fields_list.count(self.fields_list[i]))
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
            self.normalized_dataset[["Date"]] = self.normalized_dataset[["Date"]].apply(pd.to_datetime)
            self.normalized_dataset = self.normalized_dataset.set_index("Date")
            self.parent.workspace.setData(self.normalized_dataset)
            self.parent.workspace.loadDataset()
            self.parent.loadTable()
            self.destroy()

    def reject(self):
        print("Reject")
        self.destroy()

# --------------------------------------------------------------------------------------------------------------------------------------------------------
class Win0(QtWidgets.QMainWindow, Ui_win0):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # ---------------------------------------------------------- Set the configuration of the tabs
        self.tabs.tabBarClicked.connect(self.newTab)
        self.setClosableTabs()
        self.tabs.tabCloseRequested.connect(self.closeTab)
        self.graph_layouts_list = [] # Stores the layouts which contains
        self.calendar = None
        self.calendar_btn = None
        self.dataset = None
        self.workspace = None

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
        self.all_acts_list.installEventFilter(self)
        self.activities_show_list.installEventFilter(self)
        self.button_add_acts.installEventFilter(self)
        self.button_quit_ops.installEventFilter(self)
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

        # ---------------------------------------------------- Others
        self.setEnabledWidgets(False)
        self.loadLastWorkspace()

    def setEnabledWidgets(self, state = True):
        self.tabs.setEnabled(state)
        self.import_menu.setEnabled(state)
        self.save_workspace_menu.setEnabled(state)
        self.saveas_workspace_menu.setEnabled(state)

    def loadWorkspace(self, workspace):
        self.workspace = workspace
        self.workspace.loadDataset()
        if len(self.workspace.dataset) > 0: #If the dataset get at least 1 record 
            self.loadTable()
        self.setEnabledWidgets(True)
        
    def loadTable(self):
        rows_num = len(self.workspace.dataset)
        cols_num = self.table1.columnCount()
        values = self.workspace.dataset.values
        print("rows_num: ", rows_num)
        if rows_num > 100: # If there are more rows than 100 (default number)
            self.table1.setRowCount(rows_num)
        for i in range(rows_num):
            for j in range(cols_num):
                self.table1.setItem(i, j, QtWidgets.QTableWidgetItem(str(values[i][j])))
        self.workspace.set_activities_labels()

    def loadLastWorkspace(self):
        last_file = open("last.txt", "r")
        file_path = last_file.read()
        if os.path.exists(file_path + ".works"):
            file = open(file_path + ".works", "rb")
            self.workspace = pickle.load(file)
            self.setEnabledWidgets(True)
            self.loadWorkspace(self.workspace)

    def importCsv(self):
        import_csv = ImportCsv(self)
        import_csv.exec_()

    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.FocusIn:
            self.mousePressEvent(event)
        elif type(obj) == type(QtWidgets.QListView()) or type(obj) == type(QtWidgets.QMenuBar()):
            if event.type() == QtCore.QEvent.MouseButtonPress:
                self.mousePressEvent(event)
        return super().eventFilter(obj, event)

    def mousePressEvent(self, event):
        self.destroyCalendar()

    def newTab(self, event):
        self.destroyCalendar()
        if event == self.tabs.count() - 1:
            new_graph = NewGraphWin(self)
            new_graph.exec_()

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
            self.calendar.show()
            self.calendar.clicked.connect(self.clickCalendar)

    def clickCalendar(self, date):
        btn_name = self.calendar_btn.objectName()
        # ------------------------------------------ Set date
        if btn_name == "button_date_from":
            self.date_from.setDate(date)
        elif btn_name == "button_date_to":
            self.date_to.setDate(date)
        else:
            self.date_selected.setDate(date)
        self.destroyCalendar()

    def destroyCalendar(self):
        if self.calendar != None:
            self.calendar.hide()
            self.calendar.destroy()
            self.calendar = None

    def newWorkspace(self):
        print("newWorkspace")
        new_workspace_win = ConfigurateWorkspace(self)
        new_workspace_win.exec_()

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





