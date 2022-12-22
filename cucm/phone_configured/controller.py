from PyQt5.QtCore import QThread
from .view import PhoneListView
from .model import PhoneModel
from .worker import PhoneWorker
from utilities.error_dialog import ErrorDialog

class PhoneConfigured():
    def __init__(self, main_window):
        self.main_window = main_window
        self.get_configured_phone()
        
    def get_configured_phone(self):
        self.main_window.main_win.progressBar.show()
        self.thread = QThread()
        self.worker = PhoneWorker(self.main_window.service)
        self.worker.api_error.connect(self.return_error)
        self.worker.finished_data.connect(self.update_phone_table)
        self.worker.start()
        
    def update_phone_table(self, data):
        model = PhoneModel(data)
        self.main_window.main_win.progressBar.hide()
        self.phone_view = PhoneListView(model)

    def return_error(self, error):
        self.main_window.main_win.progressBar.hide()
        ErrorDialog(error)