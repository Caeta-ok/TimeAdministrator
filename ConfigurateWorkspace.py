# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ConfigurateWorkspace.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ConfigurateWorkspace(object):
    def setupUi(self, ConfigurateWorkspace):
        ConfigurateWorkspace.setObjectName("ConfigurateWorkspace")
        ConfigurateWorkspace.resize(373, 302)
        ConfigurateWorkspace.setStyleSheet("color: rgb(171, 171, 171);\n"
"background-color: rgb(29, 29, 29);")
        self.dialog_buttons = QtWidgets.QDialogButtonBox(ConfigurateWorkspace)
        self.dialog_buttons.setGeometry(QtCore.QRect(119, 258, 144, 32))
        self.dialog_buttons.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.dialog_buttons.setOrientation(QtCore.Qt.Horizontal)
        self.dialog_buttons.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.dialog_buttons.setObjectName("dialog_buttons")
        self.label_service = QtWidgets.QLabel(ConfigurateWorkspace)
        self.label_service.setEnabled(True)
        self.label_service.setGeometry(QtCore.QRect(65, 113, 39, 16))
        self.label_service.setObjectName("label_service")
        self.lineedit_service = QtWidgets.QLineEdit(ConfigurateWorkspace)
        self.lineedit_service.setEnabled(False)
        self.lineedit_service.setGeometry(QtCore.QRect(110, 114, 237, 17))
        self.lineedit_service.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineedit_service.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.lineedit_service.setObjectName("lineedit_service")
        self.label_database = QtWidgets.QLabel(ConfigurateWorkspace)
        self.label_database.setGeometry(QtCore.QRect(54, 89, 47, 13))
        self.label_database.setObjectName("label_database")
        self.lineedit_pass = QtWidgets.QLineEdit(ConfigurateWorkspace)
        self.lineedit_pass.setEnabled(False)
        self.lineedit_pass.setGeometry(QtCore.QRect(110, 170, 237, 17))
        self.lineedit_pass.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.lineedit_pass.setObjectName("lineedit_pass")
        self.examin_button = QtWidgets.QPushButton(ConfigurateWorkspace)
        self.examin_button.setEnabled(False)
        self.examin_button.setGeometry(QtCore.QRect(279, 67, 70, 22))
        self.examin_button.setStatusTip("")
        self.examin_button.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.examin_button.setCheckable(False)
        self.examin_button.setAutoRepeat(False)
        self.examin_button.setDefault(False)
        self.examin_button.setObjectName("examin_button")
        self.lineedit_db_name = QtWidgets.QLineEdit(ConfigurateWorkspace)
        self.lineedit_db_name.setEnabled(False)
        self.lineedit_db_name.setGeometry(QtCore.QRect(110, 198, 237, 17))
        self.lineedit_db_name.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.lineedit_db_name.setObjectName("lineedit_db_name")
        self.checkbox_database = QtWidgets.QCheckBox(ConfigurateWorkspace)
        self.checkbox_database.setEnabled(True)
        self.checkbox_database.setGeometry(QtCore.QRect(34, 90, 13, 13))
        self.checkbox_database.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.checkbox_database.setText("")
        self.checkbox_database.setObjectName("checkbox_database")
        self.label_csv = QtWidgets.QLabel(ConfigurateWorkspace)
        self.label_csv.setGeometry(QtCore.QRect(58, 45, 47, 13))
        self.label_csv.setObjectName("label_csv")
        self.label_database_name = QtWidgets.QLabel(ConfigurateWorkspace)
        self.label_database_name.setGeometry(QtCore.QRect(25, 197, 84, 16))
        self.label_database_name.setObjectName("label_database_name")
        self.label_table_name = QtWidgets.QLabel(ConfigurateWorkspace)
        self.label_table_name.setGeometry(QtCore.QRect(45, 225, 63, 16))
        self.label_table_name.setObjectName("label_table_name")
        self.label_user = QtWidgets.QLabel(ConfigurateWorkspace)
        self.label_user.setGeometry(QtCore.QRect(77, 140, 27, 16))
        self.label_user.setObjectName("label_user")
        self.checkbox_csv = QtWidgets.QCheckBox(ConfigurateWorkspace)
        self.checkbox_csv.setEnabled(True)
        self.checkbox_csv.setGeometry(QtCore.QRect(34, 46, 13, 13))
        self.checkbox_csv.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.checkbox_csv.setText("")
        self.checkbox_csv.setObjectName("checkbox_csv")
        self.lineedit_csv = QtWidgets.QLineEdit(ConfigurateWorkspace)
        self.lineedit_csv.setEnabled(False)
        self.lineedit_csv.setGeometry(QtCore.QRect(109, 43, 239, 18))
        self.lineedit_csv.setMouseTracking(True)
        self.lineedit_csv.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineedit_csv.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lineedit_csv.setStatusTip("")
        self.lineedit_csv.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.lineedit_csv.setFrame(True)
        self.lineedit_csv.setDragEnabled(False)
        self.lineedit_csv.setObjectName("lineedit_csv")
        self.lineedit_table_name = QtWidgets.QLineEdit(ConfigurateWorkspace)
        self.lineedit_table_name.setEnabled(False)
        self.lineedit_table_name.setGeometry(QtCore.QRect(110, 226, 237, 17))
        self.lineedit_table_name.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.lineedit_table_name.setObjectName("lineedit_table_name")
        self.lineedit_user = QtWidgets.QLineEdit(ConfigurateWorkspace)
        self.lineedit_user.setEnabled(False)
        self.lineedit_user.setGeometry(QtCore.QRect(110, 142, 237, 17))
        self.lineedit_user.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.lineedit_user.setObjectName("lineedit_user")
        self.label_password = QtWidgets.QLabel(ConfigurateWorkspace)
        self.label_password.setGeometry(QtCore.QRect(56, 170, 47, 13))
        self.label_password.setObjectName("label_password")
        self.lineedit_workspace_name = QtWidgets.QLineEdit(ConfigurateWorkspace)
        self.lineedit_workspace_name.setEnabled(True)
        self.lineedit_workspace_name.setGeometry(QtCore.QRect(109, 14, 239, 18))
        self.lineedit_workspace_name.setMouseTracking(True)
        self.lineedit_workspace_name.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineedit_workspace_name.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lineedit_workspace_name.setStatusTip("")
        self.lineedit_workspace_name.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.lineedit_workspace_name.setFrame(True)
        self.lineedit_workspace_name.setDragEnabled(False)
        self.lineedit_workspace_name.setObjectName("lineedit_workspace_name")
        self.label_workspace_name = QtWidgets.QLabel(ConfigurateWorkspace)
        self.label_workspace_name.setGeometry(QtCore.QRect(16, 12, 89, 16))
        self.label_workspace_name.setObjectName("label_workspace_name")

        self.retranslateUi(ConfigurateWorkspace)
        self.dialog_buttons.accepted.connect(ConfigurateWorkspace.accept)
        self.dialog_buttons.rejected.connect(ConfigurateWorkspace.reject)
        QtCore.QMetaObject.connectSlotsByName(ConfigurateWorkspace)

    def retranslateUi(self, ConfigurateWorkspace):
        _translate = QtCore.QCoreApplication.translate
        ConfigurateWorkspace.setWindowTitle(_translate("ConfigurateWorkspace", "Configurate Workspace"))
        self.label_service.setText(_translate("ConfigurateWorkspace", "Service:"))
        self.label_database.setText(_translate("ConfigurateWorkspace", "Database"))
        self.examin_button.setText(_translate("ConfigurateWorkspace", "Examin"))
        self.label_csv.setText(_translate("ConfigurateWorkspace", "CSV"))
        self.label_database_name.setText(_translate("ConfigurateWorkspace", "Database name:"))
        self.label_table_name.setText(_translate("ConfigurateWorkspace", "Table name:"))
        self.label_user.setText(_translate("ConfigurateWorkspace", "User:"))
        self.label_password.setText(_translate("ConfigurateWorkspace", "Password:"))
        self.label_workspace_name.setText(_translate("ConfigurateWorkspace", "Workspace name:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ConfigurateWorkspace = QtWidgets.QDialog()
    ui = Ui_ConfigurateWorkspace()
    ui.setupUi(ConfigurateWorkspace)
    ConfigurateWorkspace.show()
    sys.exit(app.exec_())
