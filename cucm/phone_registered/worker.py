from PyQt5.QtCore import pyqtSignal, QThread
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