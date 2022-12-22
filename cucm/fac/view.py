

from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QMainWindow
from .fac_view import Ui_MainWindow

class FACListView(QObject):
    def __init__(self, model):
        super().__init__()
        self.window = QMainWindow()
        self.fac_win = Ui_MainWindow()
        self.fac_win.setupUi(self.window)
        self.fac_win.fac_tableView.setModel(model)
        # self.fac_win.fac_tableView.resizeColumnToContents(1)
        self.window.show()
