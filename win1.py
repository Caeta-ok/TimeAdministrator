from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_win1(object):
    flag_accept_pressed = False
    __win0_setColNames = None

    # def __init__(self, win0_setColNames):
    #     self.__win0_setColNames = win0_setColNames

    def setupUi(self, win1):
        win1.setObjectName("win1")
        win1.resize(261, 163)
        win1.setMinimumSize(QtCore.QSize(261, 163))
        win1.setMaximumSize(QtCore.QSize(261, 163))
        win1.setStyleSheet("background-color: rgb(29, 29, 29);")

        string_style_combos = "background-color: rgb(79, 79, 79);\nselection-background-color: rgb(76, 153, 0);\nselection-color: rgb(255, 238, 193);"


        self.__centralwidget = QtWidgets.QWidget(win1)
        self.__centralwidget.setObjectName("centralwidget")
        # ---------------------------------------------------------------------------------------- Date Label
        self.__label_date = QtWidgets.QLabel(self.__centralwidget)
        self.__label_date.setGeometry(QtCore.QRect(31, 11, 40, 16))
        self.__label_date.setStyleSheet("color: rgb(79, 79, 79);\n""font: 12pt \"MS Shell Dlg 2\";")
        self.__label_date.setObjectName("label_date")

        # ---------------------------------------------------------------------------------------- Date Combo Box
        self.__comboBox_date = QtWidgets.QComboBox(self.__centralwidget)
        self.__comboBox_date.setGeometry(QtCore.QRect(78, 14, 161, 16))
        self.__comboBox_date.setStyleSheet(string_style_combos)
        self.__comboBox_date.setObjectName("comboBox_date")

        # ---------------------------------------------------------------------------------------- Activity Label
        self.__label_activity = QtWidgets.QLabel(self.__centralwidget)
        self.__label_activity.setGeometry(QtCore.QRect(10, 37, 61, 16))
        self.__label_activity.setStyleSheet("color: rgb(79, 79, 79);\n""font: 12pt \"MS Shell Dlg 2\";")
        self.__label_activity.setObjectName("label_activity")

        # ---------------------------------------------------------------------------------------- Activity Combo Box
        self.__comboBox_activity = QtWidgets.QComboBox(self.__centralwidget)
        self.__comboBox_activity.setGeometry(QtCore.QRect(78, 39, 161, 16))
        self.__comboBox_activity.setStyleSheet(string_style_combos)
        self.__comboBox_activity.setObjectName("comboBox_activity")

        # ---------------------------------------------------------------------------------------- Details Label
        self.__label_details = QtWidgets.QLabel(self.__centralwidget)
        self.__label_details.setGeometry(QtCore.QRect(14, 63, 51, 16))
        self.__label_details.setStyleSheet("color: rgb(79, 79, 79);\n""font: 12pt \"MS Shell Dlg 2\";")
        self.__label_details.setObjectName("label_details")

        # ---------------------------------------------------------------------------------------- Details Combo Box
        self.__comboBox_details = QtWidgets.QComboBox(self.__centralwidget)
        self.__comboBox_details.setGeometry(QtCore.QRect(77, 65, 161, 16))
        self.__comboBox_details.setStyleSheet(string_style_combos)
        self.__comboBox_details.setObjectName("comboBox_details")

        # ---------------------------------------------------------------------------------------- Time Label
        self.__label_time = QtWidgets.QLabel(self.__centralwidget)
        self.__label_time.setGeometry(QtCore.QRect(23, 89, 44, 16))
        self.__label_time.setStyleSheet("color: rgb(79, 79, 79);\n""font: 12pt \"MS Shell Dlg 2\";")
        self.__label_time.setObjectName("label_time")

        # ---------------------------------------------------------------------------------------- Time Combo Box
        self.__comboBox_time = QtWidgets.QComboBox(self.__centralwidget)
        self.__comboBox_time.setGeometry(QtCore.QRect(77, 91, 161, 16))
        self.__comboBox_time.setStyleSheet(string_style_combos)
        self.__comboBox_time.setObjectName("comboBox_time")

        self.pushButton_accept = QtWidgets.QPushButton(self.__centralwidget)
        self.pushButton_accept.setGeometry(QtCore.QRect(73, 121, 75, 23))
        self.pushButton_accept.setStyleSheet("background-color: rgb(79, 79, 79);")
        self.pushButton_accept.setObjectName("pushButton_accept")

        self.pushButton_cancel = QtWidgets.QPushButton(self.__centralwidget)
        self.pushButton_cancel.setGeometry(QtCore.QRect(164, 121, 75, 23))
        self.pushButton_cancel.setStyleSheet("background-color: rgb(79, 79, 79);")
        self.pushButton_cancel.setObjectName("pushButton_cancel")

        win1.setCentralWidget(self.__centralwidget)
        self.__statusbar = QtWidgets.QStatusBar(win1)
        self.__statusbar.setObjectName("statusbar")
        win1.setStatusBar(self.__statusbar)
        self.__retranslateUi(win1)
        QtCore.QMetaObject.connectSlotsByName(win1)
        win1.setTabOrder(self.__comboBox_details, self.__comboBox_date)
        win1.setTabOrder(self.__comboBox_date, self.__comboBox_activity)

        # -------------------------------------------------------------------------- Set button actions
        # self.pushButton_accept.clicked.connect(self.__acceptButtonAction)
        # self.pushButton_cancel.clicked.connect(self.__acceptButtonAction)

    def __retranslateUi(self, win1):
        _translate = QtCore.QCoreApplication.translate
        win1.setWindowTitle(_translate("win1", "Select columns"))
        self.__label_date.setText(_translate("win1", "Date:"))
        self.__label_activity.setText(_translate("win1", "Activity:"))
        self.__label_details.setText(_translate("win1", "Details:"))
        self.__label_time.setText(_translate("win1", "Time:"))
        self.pushButton_accept.setText(_translate("win1", "Accept"))
        self.pushButton_cancel.setText(_translate("win1", "Cancel"))

    def setOptionsComboBoxDate(self, options = []):
        self.__comboBox_date.clear()
        for i in range(len(options)):
            self.__comboBox_date.addItem(options[i])

    def setOptionsComboBoxActivity(self, options = []):
        self.__comboBox_activity.clear()
        for i in range(len(options)):
            self.__comboBox_activity.addItem(options[i])

    def setOptionsComboBoxDetails(self, options = []):
        self.__comboBox_details.clear()
        for i in range(len(options)):
            self.__comboBox_details.addItem(options[i])

    def setOptionsComboBoxTime(self, options = []):
        self.__comboBox_time.clear()
        for i in range(len(options)):
            self.__comboBox_time.addItem(options[i])
    
    def getTextComboBoxDate(self):
        return self.__comboBox_date.currentText()

    def getTextComboBoxActivity(self):
        return self.__comboBox_activity.currentText()

    def getTextComboBoxDetails(self):
        return self.__comboBox_details.currentText()

    def getTextComboBoxTime(self):
        return self.__comboBox_time.currentText()
    

    # def __acceptButtonAction(self):
    #     date_col = self.__comboBox_date.currentText()
    #     activity_col = self.__comboBox_activity.currentText()
    #     details_col = self.__comboBox_details.currentText()
    #     time_col = self.__comboBox_time.currentText()
    #     self.__win0_setColNames(date_col, activity_col, details_col, time_col)
        
    def __cancelButtonAction(self):
        pass
    
    # def getDateCol(self):
    #     return self.__date_col
    
    # def getActivityCol(self):
    #     return self.__activity_col
    
    # def getDetailsCol(self):
    #     return self.__details_col
    
    # def getTimeCol(self):
    #     return self.__time_col
    

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     win1 = QtWidgets.QMainWindow()
#     ui = Ui_win1()
#     ui.setupUi(win1)
#     win1.show()
#     sys.exit(app.exec_())

