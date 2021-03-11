# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'warning_msg_record.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_recordWin(object):
    def setupUi(self, recordWin):
        recordWin.setObjectName("recordWin")
        recordWin.resize(204, 84)
        self.buttonBox = QtWidgets.QDialogButtonBox(recordWin)
        self.buttonBox.setGeometry(QtCore.QRect(7, 44, 164, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.No|QtWidgets.QDialogButtonBox.Yes)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(recordWin)
        self.label.setGeometry(QtCore.QRect(19, 17, 57, 16))
        self.label.setText("")
        self.label.setObjectName("label")

        self.retranslateUi(recordWin)
        self.buttonBox.accepted.connect(recordWin.accept)
        self.buttonBox.rejected.connect(recordWin.reject)
        QtCore.QMetaObject.connectSlotsByName(recordWin)

    def retranslateUi(self, recordWin):
        _translate = QtCore.QCoreApplication.translate
        recordWin.setWindowTitle(_translate("recordWin", "Record"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    recordWin = QtWidgets.QDialog()
    ui = Ui_recordWin()
    ui.setupUi(recordWin)
    recordWin.show()
    sys.exit(app.exec_())

