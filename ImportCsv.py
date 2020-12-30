# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ImportCsv.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ImportCsv(object):
    def setupUi(self, ImportCsv):
        ImportCsv.setObjectName("ImportCsv")
        ImportCsv.resize(450, 248)
        ImportCsv.setStyleSheet("background-color: rgb(29, 29, 29);\n"
"color: rgba(171, 171, 171, 171);")
        self.dialog_buttons = QtWidgets.QDialogButtonBox(ImportCsv)
        self.dialog_buttons.setGeometry(QtCore.QRect(159, 203, 156, 32))
        self.dialog_buttons.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.dialog_buttons.setOrientation(QtCore.Qt.Horizontal)
        self.dialog_buttons.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.dialog_buttons.setObjectName("dialog_buttons")
        self.comboBox_details = QtWidgets.QComboBox(ImportCsv)
        self.comboBox_details.setGeometry(QtCore.QRect(159, 117, 154, 17))
        self.comboBox_details.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.comboBox_details.setObjectName("comboBox_details")
        self.comboBox_time = QtWidgets.QComboBox(ImportCsv)
        self.comboBox_time.setGeometry(QtCore.QRect(159, 145, 154, 17))
        self.comboBox_time.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.comboBox_time.setObjectName("comboBox_time")
        self.import_button = QtWidgets.QPushButton(ImportCsv)
        self.import_button.setGeometry(QtCore.QRect(341, 27, 75, 23))
        self.import_button.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.import_button.setObjectName("import_button")
        self.label_date = QtWidgets.QLabel(ImportCsv)
        self.label_date.setGeometry(QtCore.QRect(126, 59, 29, 16))
        self.label_date.setObjectName("label_date")
        self.lineedit_directory = QtWidgets.QLineEdit(ImportCsv)
        self.lineedit_directory.setGeometry(QtCore.QRect(29, 29, 300, 18))
        self.lineedit_directory.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.lineedit_directory.setObjectName("lineedit_directory")
        self.label_time = QtWidgets.QLabel(ImportCsv)
        self.label_time.setGeometry(QtCore.QRect(126, 143, 28, 16))
        self.label_time.setObjectName("label_time")
        self.comboBox_date = QtWidgets.QComboBox(ImportCsv)
        self.comboBox_date.setGeometry(QtCore.QRect(159, 60, 154, 17))
        self.comboBox_date.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.comboBox_date.setObjectName("comboBox_date")
        self.comboBox_activity = QtWidgets.QComboBox(ImportCsv)
        self.comboBox_activity.setGeometry(QtCore.QRect(159, 88, 154, 17))
        self.comboBox_activity.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.comboBox_activity.setObjectName("comboBox_activity")
        self.label_activity = QtWidgets.QLabel(ImportCsv)
        self.label_activity.setGeometry(QtCore.QRect(113, 86, 42, 16))
        self.label_activity.setObjectName("label_activity")
        self.label_details = QtWidgets.QLabel(ImportCsv)
        self.label_details.setGeometry(QtCore.QRect(117, 115, 36, 16))
        self.label_details.setObjectName("label_details")
        self.comboBox_involved_people = QtWidgets.QComboBox(ImportCsv)
        self.comboBox_involved_people.setGeometry(QtCore.QRect(159, 173, 154, 17))
        self.comboBox_involved_people.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.comboBox_involved_people.setObjectName("comboBox_involved_people")
        self.label_involved_people = QtWidgets.QLabel(ImportCsv)
        self.label_involved_people.setGeometry(QtCore.QRect(72, 172, 81, 16))
        self.label_involved_people.setObjectName("label_involved_people")

        self.retranslateUi(ImportCsv)
        self.dialog_buttons.accepted.connect(ImportCsv.accept)
        self.dialog_buttons.rejected.connect(ImportCsv.reject)
        QtCore.QMetaObject.connectSlotsByName(ImportCsv)

    def retranslateUi(self, ImportCsv):
        _translate = QtCore.QCoreApplication.translate
        ImportCsv.setWindowTitle(_translate("ImportCsv", "Import From Csv"))
        self.import_button.setText(_translate("ImportCsv", "Import"))
        self.label_date.setText(_translate("ImportCsv", "Date:"))
        self.label_time.setText(_translate("ImportCsv", "Time:"))
        self.label_activity.setText(_translate("ImportCsv", "Activity:"))
        self.label_details.setText(_translate("ImportCsv", "Details:"))
        self.label_involved_people.setText(_translate("ImportCsv", "Involved People:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ImportCsv = QtWidgets.QDialog()
    ui = Ui_ImportCsv()
    ui.setupUi(ImportCsv)
    ImportCsv.show()
    sys.exit(app.exec_())

