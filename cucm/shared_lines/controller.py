from PyQt5.QtCore import QThread
from .view import ShareLineView
from .model import SharedLineModel
from .worker import GetSharedLines
from utilities.error_dialog import ErrorDialog

class SharedLines():
    def __init__(self, main_window):
        self.main_window = main_window
        self.get_shared_lines()
        
    def get_shared_lines(self):
        self.main_window.main_win.progressBar.show()
        self.thread = QThread()
        self.worker = GetSharedLines(self.main_window.service)
        self.worker.api_error.connect(self.return_error)
        self.worker.finished.connect(self.update_shared_lines_table)
        self.worker.start()
        
    def update_shared_lines_table(self, data):
        model = SharedLineModel(data)
        self.main_window.main_win.progressBar.hide()
        self.sharedlines_view = ShareLineView(model)

    def return_error(self, error):
        self.main_window.main_win.progressBar.hide()
        ErrorDialog(error)