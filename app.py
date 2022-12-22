'''
   app.py is the main entry point into the application. This also displays the main window which has all of the button to perform
   SOAP and REST API calls into CUCM/CUC and CER. 
'''
import cucm
import cuc
from app_imports import *

class MainWindow(QMainWindow):
   def __init__(self, parent=None):
      super().__init__(parent)
      self.main_win = Ui_MainWindow()
      self.main_win.setupUi(self)
      self.main_win.progressBar.hide()
      self.main_win.actionAbout.triggered.connect(self.about)

   def initializeZeep(self):
      if (self.main_win.cucm_ip_input.text() != '' and self.main_win.cucm_uname_input.text() != '' and self.main_win.cucm_pw_input.text() != ''):
         enable_cucm_btns(self)
         self.service = InitialZeep(self.main_win.cucm_ip_input.text(), self.main_win.cucm_uname_input.text(), self.main_win.cucm_pw_input.text())

   def get_phone_registration(self):
      self.phones_registered = cucm.phone_registered.controller.PhoneRegistered(self)
      
   def get_cucm_version(self):
      cucm.version.get_cucm_version(self)

   def list_phones(self):
      self.phones_configured = cucm.phone_configured.controller.PhoneConfigured(self)

   def list_siptrunks(self):
      self.get_trunks = cucm.sip_trunks.controller.list_siptrunks(self)
   
   def list_gateways(self):
      self.gateways = cucm.gateways.controller.list_gateways(self)
            
   def list_huntgroups(self):
      self.huntgroups = cucm.hunt_groups.controller.list_huntgroups(self)

   def list_callparks(self):
      self.callPark = cucm.call_park.controller.list_callparks(self)
                    
   def list_shared_lines(self):
      self.sharedlines = cucm.shared_lines.controller.SharedLines(self)
      
   def list_meetmes(self):
      self.meetMe = cucm.meet_me.controller.list_meetmes(self)
      
   def list_facs(self):
      self.fac = cucm.fac.controller.get_fac(self)
      
   def get_cuc_version(self):
      creds = {'username': self.main_win.cuc_uname_input.text(), 'ip': self.main_win.cuc_ip_input.text(), 'password': self.main_win.cuc_pw_input.text()}
      cuc.version.get_cuc_version(self, creds)
   
   def list_vm_users(self):
      creds = {'username': self.main_win.cuc_uname_input.text(), 'ip': self.main_win.cuc_ip_input.text(), 'password': self.main_win.cuc_pw_input.text()}
      self.voicemailusers = cuc.voicemail_users.controller.VoicemailUsers(self, creds)
   
   def list_call_handlers(self):
      creds = {'username': self.main_win.cuc_uname_input.text(), 'ip': self.main_win.cuc_ip_input.text(), 'password': self.main_win.cuc_pw_input.text()}
      self.callhandlers = cuc.call_handlers.controller.CallHandlers(self, creds)
   
   def get_cer_version(self):
      creds = {'username': self.main_win.cer_uname_input.text(), 'ip': self.main_win.cer_ip_input.text(), 'password': self.main_win.cer_pw_input.text()}
      version = get_cer_version(creds)
      self.main_win.cuc_ver_label.setText(version['version']) 

   def list_onsite_alerts(self):
      creds = {'username': self.main_win.cuc_uname_input.text(), 'ip': self.main_win.cuc_ip_input.text(), 'password': self.main_win.cuc_pw_input.text()}

      self.onSiteAlerts = GetOnSiteAlerts(creds)
      self.main_win.OutputListWidget.show()
      for onsiteAlerts in self.onSiteAlerts.OnSiteList:
         QListWidgetItem(onsiteAlerts['OnsiteAlertName'], self.main_win.OutputListWidget)

   def list_erl(self):
      creds = {'username': self.main_win.cuc_uname_input.text(), 'ip': self.main_win.cuc_ip_input.text(), 'password': self.main_win.cuc_pw_input.text()}
      
      self.erl = GetERL(creds)
      self.main_win.OutputListWidget.show()
      for erl in self.erl.erls:
         QListWidgetItem(erl['houseNumber'], self.main_win.OutputListWidget)

   def list_ipsubnet(self):
      creds = {'username': self.main_win.cuc_uname_input.text(), 'ip': self.main_win.cuc_ip_input.text(), 'password': self.main_win.cuc_pw_input.text()}
      
      self.ipSubnets = GetIPSubnet(creds)
      self.main_win.OutputListWidget.show()
      for ipSubnets in self.ipSubnets.get_ipsubnets:
         QListWidgetItem(ipSubnets['ERLName'], self.main_win.listWidget)
   
   def about(self):
      self.modal_window = QDialog()
      about_dialog = Ui_About()
      about_dialog.setupUi(self.modal_window)
      self.modal_window.show()
            

if __name__ == "__main__":
   disable_warnings(InsecureRequestWarning)
   app = QApplication(sys.argv)
   win = MainWindow()
   win.show()
   sys.exit(app.exec())