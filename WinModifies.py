from win0 import Ui_win0
from new_graph_win import Ui_new_graph_win
from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure

class Canvas:
    def __init__(self):
        self.fig = Figure((130, 6), dpi = 70)
        self.canvas = FigureCanvas(self.fig)
        self.graph = self.fig.add_subplot(111)

class LinearGraph(Canvas):
    def __init__(self):
        super().__init__()
        # ------------------------------------------- Example data
        x_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        y_data = [12, 45, 78, 34, 56, 78, 12, 23, 37, 40]
        self.graph.plot(x_data, y_data)

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
        # self.parent.tabs.setCurrentIndex(self.parent.tabs.count())
        self.destroy()

class Win0(QtWidgets.QMainWindow, Ui_win0):
    graph_layouts_list = []
    calendar = None
    calendar_btn = ""

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tabs.tabBarClicked.connect(self.newTab)
        self.setClosableTabs()
        self.tabs.tabCloseRequested.connect(self.closeTab)
        graph_layouts_list = []
        graph_layouts_list.append(None)
        graph_layouts_list.append(self.graph_layout)
        self.graph_layouts_list = graph_layouts_list

        self.button_date_from.clicked.connect(self.showCalendar)
        self.button_date_to.clicked.connect(self.showCalendar)
        self.button_date_selected.clicked.connect(self.showCalendar)


    def newTab(self, event):
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
        # self.tabs.addTab(tab, "+")
        self.setClosableTabs()
        # self.tabs.setCurrentIndex(self.tabs.count() - 2)
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
        # ------------------------------------------------------- Get button pressed
        self.calendar_btn = self.sender()
        coordinates = self.calendar_btn.mapTo(self, QtCore.QPoint())

        # ------------------------------------------------------- Place and set calendar
        self.calendar = QtWidgets.QCalendarWidget(self)
        self.calendar.setGeometry(coordinates.x(), coordinates.y() + 30, 280, 200)
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

        # ----------------------------------------- Destroy calendar
        self.calendar.hide()
        self.calendar.destroy()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Win0()
    ui.show()
    sys.exit(app.exec_())





