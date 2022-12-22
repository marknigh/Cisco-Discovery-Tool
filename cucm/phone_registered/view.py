from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QMainWindow
from cucm.phone_registered.phone_registration_view import Ui_PhoneRegistration

class PhoneRegistrationView(QObject): 
    def __init__(self, model):
        super().__init__()
        self.window = QMainWindow()
        self.phone_win = Ui_PhoneRegistration()
        self.phone_win.setupUi(self.window)
        self.window.show()
        self._data = model.data
        self.phone_win.Phone_Reg_View.setModel(model)
