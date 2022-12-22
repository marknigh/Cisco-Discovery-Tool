'''
    This function is used to retrieve the current version of Cisco Unity Connection
'''

from requests import get
from requests.exceptions import RequestException
from requests.auth import HTTPBasicAuth
from utilities.error_dialog import ErrorDialog
import logging

def get_cuc_version(main_window, creds):

    headers = {'Accept': 'application/json', 'Connection': 'keep_alive'}
    basic_Auth = HTTPBasicAuth(creds['username'], creds['password'])

    try:
        url = ( f'https://{creds["ip"]}/vmrest/version' )
        version_res = get(url, headers=headers, auth=basic_Auth, verify=False)
        version = version_res.json()
        main_window.main_win.cuc_ver_label.setText(version['version']) 

    except RequestException as be:
        logging.warning('get_cuc_version %s ', be)
        ErrorDialog(be)
