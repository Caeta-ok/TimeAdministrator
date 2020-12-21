# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'win2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_win2(object):
    def setupUi(self, win2):
        win2.setObjectName("win2")
        win2.resize(436, 220)
        win2.setStyleSheet("background-color: rgb(29, 29, 29);\n"
"color: rgb(171, 171, 171);")
        self.centralwidget = QtWidgets.QWidget(win2)
        self.centralwidget.setObjectName("centralwidget")
        self.lineedit_directory = QtWidgets.QLineEdit(self.centralwidget)
        self.lineedit_directory.setGeometry(QtCore.QRect(19, 18, 300, 18))
        self.lineedit_directory.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.lineedit_directory.setObjectName("lineedit_directory")
        self.import_button = QtWidgets.QPushButton(self.centralwidget)
        self.import_button.setGeometry(QtCore.QRect(331, 16, 75, 23))
        self.import_button.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.import_button.setObjectName("import_button")
        self.comboBox_date = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_date.setGeometry(QtCore.QRect(58, 51, 154, 17))
        self.comboBox_date.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.comboBox_date.setObjectName("comboBox_date")
        self.label_date = QtWidgets.QLabel(self.centralwidget)
        self.label_date.setGeometry(QtCore.QRect(25, 50, 29, 16))
        self.label_date.setObjectName("label_date")
        self.label_activity = QtWidgets.QLabel(self.centralwidget)
        self.label_activity.setGeometry(QtCore.QRect(12, 77, 42, 16))
        self.label_activity.setObjectName("label_activity")
        self.label_details = QtWidgets.QLabel(self.centralwidget)
        self.label_details.setGeometry(QtCore.QRect(16, 106, 36, 16))
        self.label_details.setObjectName("label_details")
        self.label_time = QtWidgets.QLabel(self.centralwidget)
        self.label_time.setGeometry(QtCore.QRect(25, 134, 28, 16))
        self.label_time.setObjectName("label_time")
        self.comboBox_activity = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_activity.setGeometry(QtCore.QRect(58, 79, 154, 17))
        self.comboBox_activity.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.comboBox_activity.setObjectName("comboBox_activity")
        self.comboBox_details = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_details.setGeometry(QtCore.QRect(58, 108, 154, 17))
        self.comboBox_details.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.comboBox_details.setObjectName("comboBox_details")
        self.comboBox_time = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_time.setGeometry(QtCore.QRect(58, 136, 154, 17))
        self.comboBox_time.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.comboBox_time.setObjectName("comboBox_time")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(124, 175, 75, 23))
        self.pushButton_2.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(238, 175, 75, 23))
        self.pushButton_3.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.pushButton_3.setObjectName("pushButton_3")
        win2.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(win2)
        self.statusbar.setObjectName("statusbar")
        win2.setStatusBar(self.statusbar)

        self.retranslateUi(win2)
        QtCore.QMetaObject.connectSlotsByName(win2)

    def retranslateUi(self, win2):
        _translate = QtCore.QCoreApplication.translate
        win2.setWindowTitle(_translate("win2", "Import From CSV"))
        self.import_button.setText(_translate("win2", "Import"))
        self.label_date.setText(_translate("win2", "Date:"))
        self.label_activity.setText(_translate("win2", "Activity:"))
        self.label_details.setText(_translate("win2", "Details:"))
        self.label_time.setText(_translate("win2", "Time:"))
        self.pushButton_2.setText(_translate("win2", "Accept"))
        self.pushButton_3.setText(_translate("win2", "Cancel"))


#
