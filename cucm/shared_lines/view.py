from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QMainWindow
from cucm.shared_lines.sharedline_view import Ui_MainWindow

class ShareLineView(QObject): 
    def __init__(self, model):
        super().__init__()
        self.window = QMainWindow()
        self.shared_win = Ui_MainWindow()
        self.shared_win.setupUi(self.window)
        self.window.show()
        self._data = model.data
        self.shared_win.shareline_tableView.setModel(model)
