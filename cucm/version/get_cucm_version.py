'''
    Get CUCM Version.
'''

import logging
from utilities.error_dialog import ErrorDialog

def get_cucm_version(main_window):

    try:
        GetCCMVersionRes = main_window.service.service.getCCMVersion()
        main_window.main_win.cucm_ver_label.setText(GetCCMVersionRes['return']['componentVersion']['version'])

    except BaseException as be:
        logging.warning('get_cucm_version %s ', be)
        ErrorDialog(be)
