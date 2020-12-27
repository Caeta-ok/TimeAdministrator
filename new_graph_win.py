# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_graph_win.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_new_graph_win(object):
    def setupUi(self, new_graph_win):
        new_graph_win.setObjectName("new_graph_win")
        new_graph_win.resize(188, 127)
        new_graph_win.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        new_graph_win.setStyleSheet("background-color: rgb(29, 29, 29);\n"
"color: rgb(171, 171, 171);")
        self.buttonBox = QtWidgets.QDialogButtonBox(new_graph_win)
        self.buttonBox.setGeometry(QtCore.QRect(5, 78, 166, 32))
        self.buttonBox.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.combo_box_graph_types = QtWidgets.QComboBox(new_graph_win)
        self.combo_box_graph_types.setGeometry(QtCore.QRect(14, 20, 158, 22))
        self.combo_box_graph_types.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.combo_box_graph_types.setObjectName("combo_box_graph_types")

        self.retranslateUi(new_graph_win)
        self.buttonBox.accepted.connect(new_graph_win.accept)
        self.buttonBox.rejected.connect(new_graph_win.reject)
        QtCore.QMetaObject.connectSlotsByName(new_graph_win)

    def retranslateUi(self, new_graph_win):
        _translate = QtCore.QCoreApplication.translate
        new_graph_win.setWindowTitle(_translate("new_graph_win", "New Graph"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     new_graph_win = QtWidgets.QDialog()
#     ui = Ui_new_graph_win()
#     ui.setupUi(new_graph_win)
#     new_graph_win.show()
#     sys.exit(app.exec_())

