from win0 import Ui_win0
from new_graph_win import Ui_new_graph_win
from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure
from ConfigurateWorkspace import Ui_ConfigurateWorkspace

class Workspace:
    pass
# ------------------------------------------------------------------------------------------------------------------------------------------------------------
class ConfigurateWorkspace(QtWidgets.QDialog, Ui_ConfigurateWorkspace):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.checkbox_csv.clicked.connect(self.csvClicked)
        self.checkbox_database.clicked.connect(self.databaseClicked)

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
        print("Accept")

    def reject(self):
        print("Reject")
        self.destroy()
        
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

# ---------------------------------------------------------------------------------------------------------------------------------------------------------
class Win0(QtWidgets.QMainWindow, Ui_win0):
    graph_layouts_list = []
    calendar = None
    calendar_btn = None

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # ---------------------------------------------------------- Set the configuration of the tabs
        self.tabs.tabBarClicked.connect(self.newTab)
        self.setClosableTabs()
        self.tabs.tabCloseRequested.connect(self.closeTab)

        # ---------------------------------------------------------- Store layouts of the tabs that contains the graphs
        graph_layouts_list = []
        graph_layouts_list.append(None)
        graph_layouts_list.append(self.graph_layout)
        self.graph_layouts_list = graph_layouts_list

        # ----------------------------------------------------------- Set calendar buttons function
        self.button_date_from.clicked.connect(self.showCalendar)
        self.button_date_to.clicked.connect(self.showCalendar)
        self.button_date_selected.clicked.connect(self.showCalendar)

        # ----------------------------------------------------------- Set the Event Filter for the widgets
        self.spin_hours.installEventFilter(self)
        self.spin_hours_2.installEventFilter(self)
        self.spin_hours_3.installEventFilter(self)
        self.spin_min.installEventFilter(self)
        self.spin_min_2.installEventFilter(self)
        self.spin_min_3.installEventFilter(self)
        self.spin_sec.installEventFilter(self)
        self.spin_sec_2.installEventFilter(self)
        self.spin_sec_3.installEventFilter(self)
        self.all_acts_list.installEventFilter(self)
        self.activities_show_list.installEventFilter(self)
        self.button_add_acts.installEventFilter(self)
        self.button_quit_ops.installEventFilter(self)
        self.combo_box_ops_date.installEventFilter(self)
        self.combo_box_ops_time.installEventFilter(self)
        self.default_button.installEventFilter(self)
        self.new_button.installEventFilter(self)
        self.update_button.installEventFilter(self)
        self.unselect_button.installEventFilter(self)
        self.delete_button.installEventFilter(self)
        self.activity_line_edit.installEventFilter(self)
        self.text_description.installEventFilter(self)
        self.table1.installEventFilter(self)
        self.date_from.installEventFilter(self)
        self.date_to.installEventFilter(self)
        self.menubar.installEventFilter(self)

        # ----------------------------------------------------- Set menu bar configuration
        self.new_workspace_menu.triggered.connect(self.newWorkspace)

    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.FocusIn:
            self.mousePressEvent(event)
        elif type(obj) == type(QtWidgets.QListView()) or type(obj) == type(QtWidgets.QMenuBar()):
            if event.type() == QtCore.QEvent.MouseButtonPress:
                self.mousePressEvent(event)
        return super().eventFilter(obj, event)

    def mousePressEvent(self, event):
        if self.calendar != None:
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
        self.calendar.hide()
        self.calendar.destroy()
        self.calendar = None
    
    def newWorkspace(self):
        print("newWorkspace")
        new_workspace_win = ConfigurateWorkspace(self)
        new_workspace_win.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Win0()
    ui.show()
    app.setStyle("Fusion")
    sys.exit(app.exec_())





