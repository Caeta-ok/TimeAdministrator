# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'win1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_win1(object):

    def setupUi(self, win1):
        win1.setObjectName("win1")
        win1.resize(261, 163)
        win1.setMinimumSize(QtCore.QSize(261, 163))
        win1.setMaximumSize(QtCore.QSize(261, 163))
        win1.setStyleSheet("background-color: rgb(29, 29, 29);")

        string_style_combos = "background-color: rgb(79, 79, 79);\nselection-background-color: rgb(76, 153, 0);\nselection-color: rgb(255, 238, 193);"


        self.centralwidget = QtWidgets.QWidget(win1)
        self.centralwidget.setObjectName("centralwidget")
        # ---------------------------------------------------------------------------------------- Date Label
        self.label_date = QtWidgets.QLabel(self.centralwidget)
        self.label_date.setGeometry(QtCore.QRect(31, 11, 40, 16))
        self.label_date.setStyleSheet("color: rgb(79, 79, 79);\n""font: 12pt \"MS Shell Dlg 2\";")
        self.label_date.setObjectName("label_date")

        # ---------------------------------------------------------------------------------------- Date Combo Box
        self.comboBox_date = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_date.setGeometry(QtCore.QRect(78, 14, 161, 16))
        self.comboBox_date.setStyleSheet(string_style_combos)
        self.comboBox_date.setObjectName("comboBox_date")

        # ---------------------------------------------------------------------------------------- Activity Label
        self.label_activity = QtWidgets.QLabel(self.centralwidget)
        self.label_activity.setGeometry(QtCore.QRect(10, 37, 61, 16))
        self.label_activity.setStyleSheet("color: rgb(79, 79, 79);\n""font: 12pt \"MS Shell Dlg 2\";")
        self.label_activity.setObjectName("label_activity")

        # ---------------------------------------------------------------------------------------- Activity Combo Box
        self.comboBox_activity = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_activity.setGeometry(QtCore.QRect(78, 39, 161, 16))
        self.comboBox_activity.setStyleSheet(string_style_combos)
        self.comboBox_activity.setObjectName("comboBox_activity")

        # ---------------------------------------------------------------------------------------- Details Label
        self.label_details = QtWidgets.QLabel(self.centralwidget)
        self.label_details.setGeometry(QtCore.QRect(14, 63, 51, 16))
        self.label_details.setStyleSheet("color: rgb(79, 79, 79);\n""font: 12pt \"MS Shell Dlg 2\";")
        self.label_details.setObjectName("label_details")

        # ---------------------------------------------------------------------------------------- Details Combo Box
        self.comboBox_details = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_details.setGeometry(QtCore.QRect(77, 65, 161, 16))
        self.comboBox_details.setStyleSheet(string_style_combos)
        self.comboBox_details.setObjectName("comboBox_details")

        # ---------------------------------------------------------------------------------------- Time Label
        self.label_time = QtWidgets.QLabel(self.centralwidget)
        self.label_time.setGeometry(QtCore.QRect(23, 89, 44, 16))
        self.label_time.setStyleSheet("color: rgb(79, 79, 79);\n""font: 12pt \"MS Shell Dlg 2\";")
        self.label_time.setObjectName("label_time")

        # ---------------------------------------------------------------------------------------- Time Combo Box
        self.comboBox_time = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_time.setGeometry(QtCore.QRect(77, 91, 161, 16))
        self.comboBox_time.setStyleSheet(string_style_combos)
        self.comboBox_time.setObjectName("comboBox_time")

        self.pushButton_accept = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_accept.setGeometry(QtCore.QRect(73, 121, 75, 23))
        self.pushButton_accept.setStyleSheet("background-color: rgb(79, 79, 79);")
        self.pushButton_accept.setObjectName("pushButton_accept")

        self.pushButton_cancel = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_cancel.setGeometry(QtCore.QRect(164, 121, 75, 23))
        self.pushButton_cancel.setStyleSheet("background-color: rgb(79, 79, 79);")
        self.pushButton_cancel.setObjectName("pushButton_cancel")

        win1.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(win1)
        self.statusbar.setObjectName("statusbar")
        win1.setStatusBar(self.statusbar)
        self.retranslateUi(win1)
        QtCore.QMetaObject.connectSlotsByName(win1)
        win1.setTabOrder(self.comboBox_details, self.comboBox_date)
        win1.setTabOrder(self.comboBox_date, self.comboBox_activity)

        # -------------------------------------------------------------------------- Set button actions
        self.pushButton_accept.clicked.connect(self.acceptButtonAction)
        self.pushButton_cancel.clicked.connect(self.acceptButtonAction)

    def retranslateUi(self, win1):
        _translate = QtCore.QCoreApplication.translate
        win1.setWindowTitle(_translate("win1", "Select columns"))
        self.label_date.setText(_translate("win1", "Date:"))
        self.label_activity.setText(_translate("win1", "Activity:"))
        self.label_details.setText(_translate("win1", "Details:"))
        self.label_time.setText(_translate("win1", "Time:"))
        self.pushButton_accept.setText(_translate("win1", "Accept"))
        self.pushButton_cancel.setText(_translate("win1", "Cancel"))

    def setOptionsComboBoxDate(self, options = []):
        self.comboBox_date.clear()
        for i in range(len(options)):
            self.comboBox_date.addItem(options[i])

    def setOptionsComboBoxActivity(self, options = []):
        self.comboBox_activity.clear()
        for i in range(len(options)):
            self.comboBox_activity.addItem(options[i])

    def setOptionsComboBoxDetails(self, options = []):
        self.comboBox_details.clear()
        for i in range(len(options)):
            self.comboBox_details.addItem(options[i])

    def setOptionsComboBoxTime(self, options = []):
        self.comboBox_time.clear()
        for i in range(len(options)):
            self.comboBox_time.addItem(options[i])
    
    def acceptButtonAction(self):
        print(self.comboBox_date.currentText())
        print(self.comboBox_activity.currentText())
        print(self.comboBox_details.currentText())
        print(self.comboBox_time.currentText())

    def cancelButtonAction(self):
        pass



# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     win1 = QtWidgets.QMainWindow()
#     ui = Ui_win1()
#     ui.setupUi(win1)
#     win1.show()
#     sys.exit(app.exec_())

