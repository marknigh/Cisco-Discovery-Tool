

from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QMainWindow
from .meetme_view import Ui_MainWindow


class MeetMeListView(QObject): 
    def __init__(self, model):
        super().__init__()
        self.window = QMainWindow()
        self.meetme_win = Ui_MainWindow()
        self.meetme_win.setupUi(self.window)
        self.meetme_win.meetme_tableView.setModel(model)
        self.meetme_win.meetme_tableView.resizeColumnToContents(2)
        self.window.show()
