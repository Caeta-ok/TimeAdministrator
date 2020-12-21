import win0 as w0
import win1 as w1
import win2 as w2
from PyQt5.QtWidgets import QMainWindow, QApplication, QMenu

class Main(QMainWindow, w0.Ui_win0):
    win0 = None
    __win0_ui = None

    def __init__(self):
        self.win0 = QMainWindow()
        self.__win0_ui = w0.Ui_win0()
        self.__win0_ui.setupUi(self.win0)
        self.win0.show()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    main = Main()
    app.setStyle("Fusion")
    sys.exit(app.exec_())

