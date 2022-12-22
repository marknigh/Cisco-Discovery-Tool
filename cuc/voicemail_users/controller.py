from PyQt5.QtCore import QThread
from .view import VoicemailUserView
from .model import VoicemailUserModel
from .worker import VoicemailUserWorker
from utilities.error_dialog import ErrorDialog

class VoicemailUsers():
    def __init__(self, main_window, creds):
        self.main_window = main_window
        self.creds = creds
        self.get_voicemail_users()
        
    def get_voicemail_users(self):
        self.main_window.main_win.progressBar.show()
        self.thread = QThread()
        self.worker = VoicemailUserWorker(self.creds)
        self.worker.api_error.connect(self.return_error)
        self.worker.finished.connect(self.update_phone_table)
        self.worker.start()
        
    def update_phone_table(self, data):
        model = VoicemailUserModel(data)
        self.main_window.main_win.progressBar.hide()
        self.voicemailusers_view = VoicemailUserView(model)

    def return_error(self, error):
        self.main_window.main_win.progressBar.hide()
        ErrorDialog(error)