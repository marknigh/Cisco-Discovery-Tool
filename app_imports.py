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
from get_callhandlers import CallHandlerWorker, CallHandlerView, CallHandlerModel
from get_callpark import GetCallPark
from get_cucm_version import get_cucm_version
from get_cuc_version import get_cuc_version
from get_cer_version import get_cer_version
from get_erl import GetERL
from get_fac import GetFAC
from get_gateways import GetGateways
from get_huntgroups import GetHuntGroups
from get_ipsubnet import GetIPSubnet
from get_meetme import GetMeetMe
from get_onsite_alerts import GetOnSiteAlerts
from get_phone_registration import PhoneRegistrationWorker, PhoneRegistrationView, PhoneRegistrationModel 
from get_phones import PhoneListView, PhoneModel, PhoneWorker
from get_shared_lines import GetSharedLines
from get_trunks import GetTrunks
from get_vm_users import VoicemailUserWorker, VoicemailUserView, VoicemailUserModel
from initial_ris_zeep import InitialRISZeep
from initial_zeep import InitialZeep
from main_window import Ui_MainWindow
from about import Ui_About
from error_dialog import ErrorDialog
from build_gateway_tree import BuildGatewayWindow
from build_hg_tree import BuildHuntGroup
