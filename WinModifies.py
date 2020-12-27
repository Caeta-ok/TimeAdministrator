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
        self.parent.tabs.setCurrentIndex(self.parent.tabs_number)
        self.destroy()

class Win0(QtWidgets.QMainWindow, Ui_win0):
    tabs_number = 0
    tabs_list = []
    graph_layouts_list = []
    flag_close_tab = False

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        tabs_list = []
        tabs_list.append(self.tab1)
        tabs_list.append(self.tab2)
        self.tabs_list = tabs_list
        self.tabs_number = len(tabs_list)
        graph_layouts_list = []
        graph_layouts_list.append(None)
        graph_layouts_list.append(self.graph_layout)
        self.graph_layouts_list = graph_layouts_list
        self.tabs.tabBarClicked.connect(self.newTab)

    def newTab(self, event):
        if event == self.tabs_number - 1:
            new_graph = NewGraphWin(self)
            new_graph.exec_()

    def closeTab(self, event):
        print("Close tab: " + str(event))
        # widget = self.tabs.widget()
        if self.flag_close_tab == False:
            self.tabs.removeTab(event)
            self.flag_close_tab = True
        else:
            self.flag_close_tab = False

    def createNewTab(self):
        tab = QtWidgets.QWidget()
        self.tabs.addTab(tab, "+")
        # --------------------------------------- Set the closable tabs
        self.tabs.setTabsClosable(False)
        self.tabs.setTabsClosable(True)
        self.tabs.tabBar().setTabButton(0, QtWidgets.QTabBar.RightSide, None)
        self.tabs.tabBar().setTabButton(self.tabs_number, QtWidgets.QTabBar.RightSide, None)

        # -------------------------------------- Set the close tabs functionality
        # self.tabs.tabCloseRequested(self.tabs_number - 1).connect(self.closeTab)
        self.tabs.tabCloseRequested.connect(self.closeTab)
        # self.tabs.tabBar().tabCloseRequested(self.tabs_number - 1).connect(self.closeTab)
        print("new tab")

        # -------------------------------------- Add tab to the list
        tabs_list = self.tabs_list
        tabs_list.append(tab)
        self.tabs_list = tabs_list

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

        # -------------------------------------- Set the number of tabs
        self.tabs_number += 1
        
    def createLinearGraph(self):
        self.createNewTab()
        linear_graph = LinearGraph()
        self.graph_layouts_list[self.tabs_number - 2].addWidget(linear_graph.canvas)

        self.tabs.setTabText(self.tabs_number - 2, "Linear Graph")
        self.tabs.setCurrentIndex(self.tabs_number - 2)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Win0()
    ui.show()
    sys.exit(app.exec_())





