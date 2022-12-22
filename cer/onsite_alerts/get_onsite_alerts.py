'''
    This class will retrieve Onsite Alert emails from CER. An onsite alert is a notification to on-site (security) personnel via IP phone and/or email
'''
import requests
from requests.auth import HTTPBasicAuth
from utilities.error_dialog import ErrorDialog
import logging
class GetOnSiteAlerts:
    def __init__(self, creds):
        self._ip = creds['ip']
        self._basic_auth = HTTPBasicAuth(creds['username'], creds['password'])
        self.OnSiteList = []

        self.get_onsite_alerts()
        
    def get_onsite_alerts(self):
       
        headers = {'Accept': 'application/json', 'Connection': 'keep_alive'}
        
        try:
            response = requests.get(f'https://{self._ip}/cerappservices/service/cerl', headers=headers, auth=self._basic_auth, verify=False)
            response_json = response.json()
            for detail in response_json['onsitealert']['details']:
                self.OnSiteList.append({
                    'Onsite Alert': detail['OnsiteAlertID'],
                    'Name': detail['OnsiteAlertName'],
                    'Number:': detail['OnsiteAlertNum'],
                    'Email': detail['OnsiteAlertEmail']
                })
    
        except BaseException as be:
            logging.warning('get_onsite_alerts %s ', be)
            open = ErrorDialog(be)
            open.exec()
