from PyQt5.QtCore import QThread
from .view import CallHandlerView
from .model import CallHandlerModel
from .worker import CallHandlerWorker
from utilities.error_dialog import ErrorDialog

class CallHandlers():
    def __init__(self, main_window, creds):
        self.main_window = main_window
        self.creds = creds
        self.get_callhandlers()
        
    def get_callhandlers(self):
        self.main_window.main_win.progressBar.show()
        self.thread = QThread()
        self.worker = CallHandlerWorker(self.creds)
        self.worker.api_error.connect(self.return_error)
        self.worker.finished.connect(self.update_callhandler_table)
        self.worker.start()
        
    def update_callhandler_table(self, data):
        model = CallHandlerModel(data)
        self.main_window.main_win.progressBar.hide()
        self.voicemailusers_view = CallHandlerView(model)

    def return_error(self, error):
        self.main_window.main_win.progressBar.hide()
        ErrorDialog(error)



