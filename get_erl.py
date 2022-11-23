'''
    This class is to retreive all ERLs from the configuration Emergency Responder Server.
    This is currently BETA 
'''

import requests
from requests.auth import HTTPBasicAuth
from error_dialog import ErrorDialog
import logging

class GetERL:
    def __init__(self, creds):
        self._ip = creds['ip']
        self.erls = []
        self._basic_auth = HTTPBasicAuth(creds['username'], creds['password'])

        self.get_erl()
        
    def get_erl(self):

        headers = {'Accept': 'application/json', 'Connection': 'keep_alive'}

        try:
            response = requests.get(f'https://{self._ip}/cerappservices/export/conventionalerl/info', headers=headers, auth=self._basic_auth, verify=False)
            response_json = response.json()
            for erl_info in response_json['ConventionalERL']['ERLDetails']:
                self.erls.append({
                    'Erl Name': erl_info['ERLName'],
                    "ELIN": erl_info['ELINSettings'],
                    'House Number': erl_info['ALIInfo']['HouseNumber']
                    })
        
        except BaseException as be:
            logging.warning('get_erl %s ', be)
            open = ErrorDialog(be)
            open.exec()

