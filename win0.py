import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import pandas as pd
import win1 as w1

qtCreatorFile = "win0.ui"
Ui_win0, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_win0):
    __date_col_name = ""
    __activity_col_name = ""
    __details_col_name = ""
    __time_col_name = ""

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.win0 = Ui_win0.__init__(self)
        self.setupUi(self)
        self.actionOpen_csv.triggered.connect(self.openCsv)

    def openCsv(self):
        def setColNames(): # Set the column names of which getting the data
            self.__date_col_name = ui.getTextComboBoxDate()
            self.__activity_col_name = ui.getTextComboBoxActivity()
            self.__details_col_name = ui.getTextComboBoxDetails()
            self.__time_col_name = ui.getTextComboBoxTime()
            self.win1.close()
            self.win1.destroy()

        # ----------------------------------------------------- Open file
        fname = QFileDialog.getOpenFileName(self, "Open file", "C:\\Users\\Caeta\\Desktop\\Documentos\\Proyectos\\TimeAdministrator")
        dataset = pd.read_csv(fname[0], sep = ";")

        # ----------------------------------------------------- Create a secondary window
        self.win1 = QtWidgets.QMainWindow()
        ui = w1.Ui_win1()
        ui.setupUi(self.win1)
        self.win1.show()

        # ----------------------------------------------------- Configurate options of combo boxes
        options = dataset.columns.tolist()
        ui.setOptionsComboBoxDate(options)
        ui.setOptionsComboBoxActivity(options)
        ui.setOptionsComboBoxDetails(options)
        ui.setOptionsComboBoxTime(options)

        ui.pushButton_accept.clicked.connect(setColNames)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())





