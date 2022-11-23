'''
    This module represents the MVC for getting all voicemail users from Unity Connection.  
'''

import requests
from requests.auth import HTTPBasicAuth
from PyQt5.QtCore import QThread, pyqtSignal, QAbstractTableModel, Qt
from PyQt5.QtWidgets import QMainWindow
from vm_users_windows import Ui_VoiceMailUsers
import logging

class VoicemailUserWorker(QThread):
    finished_download = pyqtSignal(list)
    api_error = pyqtSignal(object)
    
    def __init__(self, creds):
        super().__init__()
        self._ip = creds['ip']
        self._headers = {'Accept': 'application/json', 'Connection': 'keep_alive'}
        self._basic_Auth = HTTPBasicAuth(creds['username'], creds['password'])

        self.vmUserList = []
    
    def run(self):
        try:
            url = ( f'https://{self._ip}/vmrest/users/' )
            users_res = requests.get(url, headers=self._headers, auth=self._basic_Auth, verify=False)
            items = users_res.json()
            for item in items['User']:
                vm_user_dict = {
                    'Display': item['DisplayName'],
                    'URI': item['URI']
                    }
                self.vmUserList.append(vm_user_dict)

            self.finished_download.emit(self.vmUserList)
                    
        except BaseException as be:
            logging.warning('get_vm_users %s', be)
            self.api_error.emit(be)
    
class VoicemailUserView:
    def __init__(self, model):
        super().__init__()
        self._model = model
        #Set up User interface from designer
        self.window = QMainWindow()
        self.vmwin = Ui_VoiceMailUsers()
        self.vmwin.setupUi(self.window)
        self.window.show()
        self.vmwin.tableView.setModel(self._model)
        # self.vmwin.tableView.doubleClicked.connect(self.user_detail) 
        
    # def user_detail(self):
    #     print('double-click')
    #     print(self._model)
    #     indexes = self.vmwin.tableView.selectedIndexes()
    #     row = self.vmwin.vmUserTable.currentIndex().row()
    #     column = self.vmwin.vmUserTable.currentIndex().column()
    #     item = self.vmwin.vmUserTable.item(row, column)
    #     print(item.text())
    #     for sub in self.vmUserList:
    #         if sub['DisplayName'] == item.text():
    #             print (sub)
    
class VoicemailUserModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.headers = ['Display', 'URI']
        
    def rowCount(self, n):
        return len(self.data)
    
    def columnCount(self, n):
        return 2

    def data(self,index,role):
        if role == Qt.DisplayRole:
            column = index.column()
            return self.data[index.row()][self.headers[column]]        