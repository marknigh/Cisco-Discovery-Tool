
'''
    Class to retrieve via CUC REST API all CallHandlers configured in Cisco Unity Connection.
    Create PyQt5 signal on table row to retreive details on CallHandler
'''
import requests
from requests.auth import HTTPBasicAuth
from PyQt5.QtCore import QObject, QAbstractTableModel, Qt, pyqtSignal, QThread
from PyQt5.QtWidgets import QMainWindow
from cuc.call_handlers.callhandler_window import Ui_Call_Handlers
from utilities.error_dialog import ErrorDialog
import logging

class CallHandlerWorker(QThread):
    finished_download = pyqtSignal(list)
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

            self.finished_download.emit(self.callHandlersList)

        except BaseException as be:
            logging.warning('get_callhandlers %s', be)
            self.api_error.emit(be)
            
class CallHandlerView(QObject):
    def __init__(self, model):
        super().__init__()
        
        #Set up User interface from designer
        self.window = QMainWindow()
        self.chwin = Ui_Call_Handlers()
        self.chwin.setupUi(self.window)
        self.window.show()
        self.chwin.tableView.setModel(model)
        # self.chwin.tableView.doubleClicked.connect(self.call_handler_details)
                        
    # def call_handler_details(self):
    #     row = self.chwin.tableView.currentIndex().row()
    #     url = ( f'https://{self._ip}' + self.chwin.tableView.item(row, 1).text())
        
    #     try:
    #         users_res = requests.get(url, headers=self._headers, auth=self._basic_auth, verify=False)
    #         user_json = users_res.json()
            
    #         try:
    #             url = ( f'https://{self._ip}' + user_json['MenuEntriesURI'] )
    #             menuEntries = requests.get(url, headers=self._headers, auth=self._basic_auth, verify=False)
    #             print(menuEntries)

    #         except BaseException as be:
    #             open = ErrorDialog(be)
    #             open.exec()
        
        # except BaseException as be:
        #     open = ErrorDialog(be)
        #     open.exec()

class CallHandlerModel(QAbstractTableModel):
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
        
        