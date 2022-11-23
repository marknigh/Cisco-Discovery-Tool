"""
    The RisPort70 (Real-Time Information Port) service provides an API for querying the current connection status of phones, 
    devices, and applications connected to Cisco Unified Communications Manager (Unified CM)
"""

from PyQt5.QtCore import QObject, QAbstractTableModel, Qt, pyqtSignal, QThread
from PyQt5.QtWidgets import QMainWindow
from phone_registration_view import Ui_PhoneRegistration
import logging

class PhoneRegistrationWorker(QThread):
    finished = pyqtSignal(list)
    api_error = pyqtSignal(object)
    
    def __init__(self, service):
        super().__init__()
        self._service = service
        self.phones = []
       
        self.CmSelectionCriteria = {
            'MaxReturnedDevices': '1000',
            'DeviceClass': 'Phone',
            'Model': '255',
            'Status': 'Any',
            'NodeName': '',
            'SelectBy': 'Name',
            'SelectItems': {
                'item': []
            },
            'Protocol': 'Any',
            'DownloadStatus': 'Any'
        }
                       
    def run(self):
        try:
            response = self._service.service.selectCmDevice( CmSelectionCriteria = self.CmSelectionCriteria, StateInfo = '')

            if response['SelectCmDeviceResult']['TotalDevicesFound'] > 0:
                for item in response['SelectCmDeviceResult']['CmNodes']['item'][0]['CmDevices']['item']:
                    self.phones.append({
                        'Name': item['Name'],
                        'Status': item['Status'],
                        'DirNumber': item['DirNumber'],
                        'IPAddress': item['IPAddress']['item'][0]['IP']
                    })                
        
            self.finished.emit(self.phones)
        
        except BaseException as be:
            logging.warning('get_phone_registration: %s', be)
            self.api_error.emit(be)
                    
class PhoneRegistrationView(QObject): 
    def __init__(self, model):
        super().__init__()
        self.window = QMainWindow()
        self.phone_win = Ui_PhoneRegistration()
        self.phone_win.setupUi(self.window)
        self.window.show()
        self._data = model.data
        self.phone_win.Phone_Reg_View.setModel(model)
    
class PhoneRegistrationModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.headers = ['Name', 'Status', 'DirNumber', 'IPAddress']
        
    def rowCount(self, n):
        return len(self.data)
    
    def columnCount(self, n):
        return 4

    def data(self,index,role):
        if role == Qt.DisplayRole:
            column = index.column()
            return self.data[index.row()][self.headers[column]]