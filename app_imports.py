import sys
if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    print('running in a PyInstaller bundle')
else:
    print('running in a normal Python process')

import logging
logging.basicConfig(filename='cisco_extract_data.log', format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)

from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QApplication, QDialog, QListWidgetItem, QMainWindow
from PyQt5.uic import loadUi
from urllib3 import disable_warnings
from urllib3.exceptions import InsecureRequestWarning
from main_window import Ui_MainWindow
from cer.get_cer_version import get_cer_version
from cer.erl.get_erl import GetERL
from cer.onsite_alerts.get_onsite_alerts import GetOnSiteAlerts
from cer.subnets.get_ipsubnet import GetIPSubnet
from utilities.initial_ris_zeep import InitialRISZeep
from utilities.initial_zeep import InitialZeep
from utilities.about import Ui_About
from utilities.error_dialog import ErrorDialog
from utilities.enable_cucm_btns import enable_cucm_btns