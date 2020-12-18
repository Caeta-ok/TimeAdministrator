import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import pandas as pd
import win1 as w1

qtCreatorFile = "win0.ui"
Ui_win0, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_win0):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.win0 = Ui_win0.__init__(self)
        self.setupUi(self)
        self.actionOpen_csv.triggered.connect(self.openCsv)

    def openCsv(self):
        # ----------------------------------------------------- Open file
        fname = QFileDialog.getOpenFileName(self, "Open file", "C:\\Users\\Caeta\\Desktop\\Documentos\\Proyectos\\TimeAdministrator")
        dataset = pd.read_csv(fname[0], sep = ";")

        # ----------------------------------------------------- Create a secondary window
        self.win1 = QtWidgets.QMainWindow()
        self.ui = w1.Ui_win1()
        self.ui.setupUi(self.win1)
        self.win1.show()

        # ----------------------------------------------------- Configurate options of combo boxes
        options = dataset.columns.tolist()
        self.ui.setOptionsComboBoxDate(options)
        self.ui.setOptionsComboBoxActivity(options)
        self.ui.setOptionsComboBoxDetails(options)
        self.ui.setOptionsComboBoxTime(options)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())





