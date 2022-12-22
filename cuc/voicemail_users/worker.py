import requests
from requests.auth import HTTPBasicAuth
from PyQt5.QtCore import QThread, pyqtSignal
import logging

class VoicemailUserWorker(QThread):
    finished = pyqtSignal(list)
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

            self.finished.emit(self.vmUserList)
                    
        except BaseException as be:
            logging.warning('get_vm_users %s', be)
            self.api_error.emit(be)