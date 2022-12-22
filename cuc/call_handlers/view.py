
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QMainWindow
from .callhandler_window import Ui_Call_Handlers


class CallHandlerView(QObject):
    def __init__(self, model):
        super().__init__()
        
        #Set up User interface from designer
        self.window = QMainWindow()
        self.chwin = Ui_Call_Handlers()
        self.chwin.setupUi(self.window)
        self.window.show()
        self.chwin.tableView.setModel(model)
        # self.chwin.tableView.doubleClicked.connect(self.call_handler_details)
