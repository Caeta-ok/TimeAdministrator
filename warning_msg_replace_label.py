# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'warning_msg_replace_label.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_warning_msg_replace_label(object):
    def setupUi(self, warning_msg_replace_label):
        warning_msg_replace_label.setObjectName("warning_msg_replace_label")
        warning_msg_replace_label.resize(190, 134)
        warning_msg_replace_label.setStyleSheet("background-color: rgb(29, 29, 29);\n"
"color: rgb(171, 171, 171);")
        self.buttonBox = QtWidgets.QDialogButtonBox(warning_msg_replace_label)
        self.buttonBox.setGeometry(QtCore.QRect(16, 91, 156, 32))
        self.buttonBox.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.No|QtWidgets.QDialogButtonBox.Yes)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(warning_msg_replace_label)
        self.buttonBox.accepted.connect(warning_msg_replace_label.accept)
        self.buttonBox.rejected.connect(warning_msg_replace_label.reject)
        QtCore.QMetaObject.connectSlotsByName(warning_msg_replace_label)

    def retranslateUi(self, warning_msg_replace_label):
        _translate = QtCore.QCoreApplication.translate
        warning_msg_replace_label.setWindowTitle(_translate("warning_msg_replace_label", "Replace Label"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     warning_msg_replace_label = QtWidgets.QDialog()
#     ui = Ui_warning_msg_replace_label()
#     ui.setupUi(warning_msg_replace_label)
#     warning_msg_replace_label.show()
#     sys.exit(app.exec_())

