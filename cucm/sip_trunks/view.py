

from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QMainWindow
from .siptrunk_view import Ui_MainWindow

class SipTrunkListView(QObject):
    def __init__(self, model):
        super().__init__()
        self.window = QMainWindow()
        self.sip_window = Ui_MainWindow()
        self.sip_window.setupUi(self.window)
        self.sip_window.siptrunk_tableView.setModel(model)
        self.sip_window.siptrunk_tableView.resizeColumnToContents(2)
        self.sip_window.siptrunk_tableView.resizeColumnToContents(3)
        self.window.show()
