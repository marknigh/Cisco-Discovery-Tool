'''
    This function is used to retrieve the current version of Cisco Emergency Responder
'''

import requests
from requests.auth import HTTPBasicAuth
from utilities.error_dialog import ErrorDialog
import logging

def get_cer_version(creds):
    
    headers = {'Accept': 'application/json', 'Connection': 'keep_alive'}
    basic_Auth = HTTPBasicAuth(creds['username'], creds['password'])

    try:
        url = ( f'https://{creds["ip"]}/cerappservices/export/cerclustergroup/list' )
        version_res = requests.get(url, headers=headers, auth=basic_Auth, verify=False)
        return version_res.json()

    except BaseException as be:
        logging.warning('get_cer_version %s ', be)
        ErrorDialog(be)
