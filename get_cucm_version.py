'''
    Get CUCM Version.
'''

import logging
from error_dialog import ErrorDialog

def get_cucm_version(service):

    try:
        GetCCMVersionRes = service.getCCMVersion()
        return(GetCCMVersionRes)

    except BaseException as be:
        logging.warning('get_cucm_version %s ', be)
        ErrorDialog(be)
