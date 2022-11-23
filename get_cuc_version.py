'''
    This function is used to retrieve the current version of Cisco Unity Connection
'''

from requests import get
from requests.exceptions import RequestException
from requests.auth import HTTPBasicAuth
from error_dialog import ErrorDialog
import logging

def get_cuc_version(creds):

    headers = {'Accept': 'application/json', 'Connection': 'keep_alive'}
    basic_Auth = HTTPBasicAuth(creds['username'], creds['password'])

    try:
        url = ( f'https://{creds["ip"]}/vmrest/version' )
        version_res = get(url, headers=headers, auth=basic_Auth, verify=False)
        return version_res.json()

    except RequestException as be:
        logging.warning('get_cuc_version %s ', be)
        ErrorDialog(be)
