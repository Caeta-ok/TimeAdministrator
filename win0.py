from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget, QFrame, QMenu, QMainWindow, qApp
import widget1 as wg1
  
# class Ui_win0(QMainWindow):
class Ui_win0(object):
    def setupUi(self, win0):
        win0.setObjectName("win0")
        win0.resize(703, 757)
        win0.setStyleSheet("background-color: rgba(29, 29, 29);"
                           "\ncolor: rgb(171, 171, 171);")
        self.centralwidget = QtWidgets.QWidget(win0)
        self.centralwidget.setObjectName("centralwidget")

        self.table1 = QTableWidget(self.centralwidget)
        self.table1.setGeometry(QtCore.QRect(30, 25, 448, 586))
        self.table1.setStyleSheet("background-color: rgba(100, 100, 100, 100);\nborder-color: rgb(47, 47, 47);"
                                  "\ngridline-color: rgb(255, 255, 255);\ncolor: rgb(100, 100, 100);"
                                  "\ngridline-color: rgb(40, 40, 40);")

        self.table1.setRowCount(100)
        self.table1.setColumnCount(4)
        self.table1.setObjectName("table1")
        item = QtWidgets.QTableWidgetItem()
        self.table1.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table1.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table1.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table1.setHorizontalHeaderItem(3, item)
        self.table1.horizontalHeader().setDefaultSectionSize(100)
        self.table1.verticalHeader().setDefaultSectionSize(20)
        self.table1.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        win0.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(win0)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 703, 21))
        self.menubar.setObjectName("menubar")
        self.menuNew = QtWidgets.QMenu(self.menubar)
        self.menuNew.setObjectName("menuNew")
        self.menuImport = QtWidgets.QMenu(self.menubar)
        self.menuImport.setObjectName("menuImport")
        win0.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(win0)
        self.statusbar.setObjectName("statusbar")
        win0.setStatusBar(self.statusbar)
        self.new_workspace_menu = QtWidgets.QAction(win0)
        self.new_workspace_menu.setObjectName("new_workspace_menu")
        self.open_workspace_menu = QtWidgets.QAction(win0)
        self.open_workspace_menu.setObjectName("open_workspace_menu")
        self.save_workspace_menu = QtWidgets.QAction(win0)
        self.save_workspace_menu.setObjectName("save_workspace_menu")
        self.saveas_workspace_menu = QtWidgets.QAction(win0)
        self.saveas_workspace_menu.setObjectName("saveas_workspace_menu")
        self.import_menu = QtWidgets.QAction(win0)
        self.import_menu.setObjectName("import_menu")
        self.menuNew.addAction(self.new_workspace_menu)
        self.menuNew.addAction(self.open_workspace_menu)
        self.menuNew.addAction(self.save_workspace_menu)
        self.menuNew.addAction(self.saveas_workspace_menu)
        self.menuImport.addAction(self.import_menu)
        self.menubar.addAction(self.menuNew.menuAction())
        self.menubar.addAction(self.menuImport.menuAction())

        self.centralwidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.table1.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)

        self.table1.customContextMenuRequested.connect(self.tableContextMenu)
        # self.centralwidget.customContextMenuRequested.connect(self.windowContextMenu)
        self.retranslateUi(win0)
        QtCore.QMetaObject.connectSlotsByName(win0)

    def tableContextMenu(self):
        menu = QMenu()
        new_reg = menu.addAction("New Time Register")
        del_reg = menu.addAction("Delete Time Register")
        mod_reg = menu.addAction("Modify Register")
        action = menu.exec_(QtGui.QCursor.pos())
        
        # if action == new_reg:
        #     print("New register")
        # elif action == option2:
        #     print("Option 2")
        
    # def windowContextMenu(self):
    #     menu = QMenu()
    #     menu.addAction("Other Option")
    #     menu.exec_(QtGui.QCursor.pos())


    def retranslateUi(self, win0):
        _translate = QtCore.QCoreApplication.translate
        win0.setWindowTitle(_translate("win0", "Time Visualizer"))
        item = self.table1.horizontalHeaderItem(0)
        item.setText(_translate("win0", "Date"))
        item = self.table1.horizontalHeaderItem(1)
        item.setText(_translate("win0", "Activity"))
        item = self.table1.horizontalHeaderItem(2)
        item.setText(_translate("win0", "Details"))
        item = self.table1.horizontalHeaderItem(3)
        item.setText(_translate("win0", "Time"))
        self.menuNew.setTitle(_translate("win0", "New"))
        self.menuImport.setTitle(_translate("win0", "Import"))
        self.new_workspace_menu.setText(_translate("win0", "New Workspace"))
        self.open_workspace_menu.setText(_translate("win0", "Open Workspace"))
        self.save_workspace_menu.setText(_translate("win0", "Save Workspace"))
        self.saveas_workspace_menu.setText(_translate("win0", "Save As Workspace"))
        self.import_menu.setText(_translate("win0", "Import From CSV"))

    # def contextMenuEvent(self, event):
    #     pass
    #     print("Context menu")
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    win0 = QtWidgets.QMainWindow()
    ui = Ui_win0()
    ui.setupUi(win0)
    win0.show()
    sys.exit(app.exec_())

