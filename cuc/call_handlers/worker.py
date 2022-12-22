import requests
from requests.auth import HTTPBasicAuth
from PyQt5.QtCore import QObject, QAbstractTableModel, Qt, pyqtSignal, QThread
from PyQt5.QtWidgets import QMainWindow
from cuc.call_handlers.callhandler_window import Ui_Call_Handlers
from utilities.error_dialog import ErrorDialog
import logging

class CallHandlerWorker(QThread):
    finished = pyqtSignal(list)
    api_error = pyqtSignal(object)

    def __init__(self, creds):
        super().__init__()
        self._ip = creds['ip']
        self._basic_auth = HTTPBasicAuth(creds['username'], creds['password'])
        self._headers = {'Accept': 'application/json', 'Connection': 'keep_alive'}
        self.callHandlersList = []

    def run(self):
        try:
            url = ( f'https://{self._ip}/vmrest/handlers/callhandlers' )
            ch_response = requests.get(url, headers=self._headers, auth=self._basic_auth, verify=False)
            ch_json = ch_response.json()
            for item in ch_json['Callhandler']:
                callhandler_dict = {
                    'Display': item['DisplayName'],
                    'URI': item['URI']
                    }
                self.callHandlersList.append(callhandler_dict)

            self.finished.emit(self.callHandlersList)

        except BaseException as be:
            logging.warning('get_callhandlers %s', be)
            self.api_error.emit(be)