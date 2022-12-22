'''
    Retreive all IP subnets configured in CER
'''
import requests
from requests.auth import HTTPBasicAuth
from utilities.error_dialog import ErrorDialog
import logging

class GetIPSubnet:
    def __init__(self, creds):
        self._ip = creds['ip']
        self.subnets = []
        self._basicAuth = HTTPBasicAuth(creds['username'], creds['password'])

        self.get_erl()
        
    def get_erl(self):

        headers = {'Accept': 'application/json', 'Connection': 'keep_alive'}

        try:
            response = requests.get(f'https://{self._ip}/cerappservices/export/ipsubnet/info', headers=headers, auth=self._basicAuth, verify=False)
            response_json = response.json()
            for subnet_info in response_json['IPSubnet']['subnetdetails']:
                self.subnets.append({
                    'SubnetID': subnet_info['subnetID'],
                    "ERLName": subnet_info['ERLName']
                    })
        
        except BaseException as be:
            logging.warning('get_ipsubnet %s ', be)
            open = ErrorDialog(be)
            open.exec()
