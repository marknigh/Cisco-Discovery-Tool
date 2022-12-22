"""
    The RisPort70 (Real-Time Information Port) service provides an API for querying the current connection status of phones, 
    devices, and applications connected to Cisco Unified Communications Manager (Unified CM)
"""

from PyQt5.QtCore import QThread
from .view import PhoneRegistrationView
from .model import PhoneRegistrationModel
from .worker import PhoneRegistrationWorker
from utilities.error_dialog import ErrorDialog
from utilities.initial_ris_zeep import InitialRISZeep

class PhoneRegistered():
    def __init__(self, main_window):
        self.main_window = main_window
        self.get_configured_phone()
        
    def get_configured_phone(self):
        service = InitialRISZeep(self.main_window.main_win.cucm_ip_input.text(),
                                 self.main_window.main_win.cucm_uname_input.text(),
                                 self.main_window.main_win.cucm_pw_input.text())
        self.main_window.main_win.progressBar.show()
        self.thread = QThread()
        self.worker = PhoneRegistrationWorker(service)
        self.worker.api_error.connect(self.return_error)
        self.worker.finished.connect(self.update_phone_table)
        self.worker.start()
        
    def update_phone_table(self, data):
        model = PhoneRegistrationModel(data)
        self.main_window.main_win.progressBar.hide()
        self.phone_view = PhoneRegistrationView(model)

    def return_error(self, error):
        self.main_window.main_win.progressBar.hide()
        ErrorDialog(error)