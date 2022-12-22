

from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QMainWindow
from .callpark_view import Ui_MainWindow

class CallParkListView(QObject):
    def __init__(self, model):
        super().__init__()
        self.window = QMainWindow()
        self.callpark_win = Ui_MainWindow()
        self.callpark_win.setupUi(self.window)
        self.callpark_win.callpark_tableView.setModel(model)
        self.callpark_win.callpark_tableView.resizeColumnToContents(1)
        self.window.show()
