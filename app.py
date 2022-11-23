'''
   app.py is the main entry point into the application. This also displays the main window which has all of the button to perform
   SOAP and REST API calls into CUCM/CUC and CER. 
'''

from app_imports import *

class MainWindow(QMainWindow):
   def __init__(self, parent=None):
      super().__init__(parent)
      self.main_win = Ui_MainWindow()
      self.main_win.setupUi(self)
      self.main_win.progressBar.hide()
      self.main_win.actionExit.triggered.connect(self.close)
      self.main_win.actionAbout.triggered.connect(self.about)

   def get_phone_registration(self):
      service = InitialRISZeep(self.main_win.cucm_ip_input.text(), self.main_win.cucm_uname_input.text(), self.main_win.cucm_pw_input.text())
      self.main_win.progressBar.show()
      self.thread = QThread()
      self.worker = PhoneRegistrationWorker(service)
      self.worker.api_error.connect(self.return_error)
      self.worker.finished.connect(self.update_phone_registration_table)
      self.worker.start()
      
   def update_phone_registration_table(self, phoneList):
      if len(phoneList) > 0:
         model = PhoneRegistrationModel(phoneList)
         self.main_win.progressBar.hide()
         self.vm_user_view = PhoneRegistrationView(model)    
      else:
         QListWidgetItem('No Phones', self.main_win.OutputListWidget)
      
   def get_cucm_version(self):
      service = InitialZeep(self.main_win.cucm_ip_input.text(), self.main_win.cucm_uname_input.text(), self.main_win.cucm_pw_input.text())
      res = get_cucm_version(service.service)
      if (res):
         self.main_win.cucm_ver_label.setText(res['return']['componentVersion']['version'])

   def list_phones(self):
      service = InitialZeep(self.main_win.cucm_ip_input.text(), self.main_win.cucm_uname_input.text(), self.main_win.cucm_pw_input.text()) 
      self.main_win.progressBar.show()
      self.thread = QThread()
      self.worker = PhoneWorker(service.service)
      self.worker.api_error.connect(self.return_error)
      self.worker.finished_data.connect(self.update_phone_table)
      self.worker.start()
   
   def return_error(self, error):
      self.main_win.progressBar.hide()
      ErrorDialog(error)
      
   def update_phone_table(self, data):
      model = PhoneModel(data)
      self.main_win.progressBar.hide()
      self.phone_view = PhoneListView(model)

   def list_siptrunks(self):
      self.main_win.OutputListWidget.clear()
      service = InitialZeep(self.main_win.cucm_ip_input.text(), self.main_win.cucm_uname_input.text(), self.main_win.cucm_pw_input.text())
      self.get_trunks = GetTrunks(service.service)
      for sipTrunks in self.get_trunks.sipTrunkList:
         singeLine = sipTrunks['name'] + ' \t ' + sipTrunks['description'] + '\t' + sipTrunks['destinations'][0]['ipv4']
         QListWidgetItem(singeLine, self.main_win.OutputListWidget)
   
   def list_gateways(self):
      service = InitialZeep(self.main_win.cucm_ip_input.text(), self.main_win.cucm_uname_input.text(), self.main_win.cucm_pw_input.text())
      gateways = GetGateways(service.service)
      self.buildGateways = BuildGatewayWindow(gateways.gatewayList)
            
   def list_huntgroups(self):
      service = InitialZeep(self.main_win.cucm_ip_input.text(), self.main_win.cucm_uname_input.text(), self.main_win.cucm_pw_input.text())
      hunt_groups = GetHuntGroups(service.service)
      self.buildHGroups = BuildHuntGroup(hunt_groups.tree_view)      
   
   def list_callparks(self):
      service = InitialZeep(self.main_win.cucm_ip_input.text(), self.main_win.cucm_uname_input.text(), self.main_win.cucm_pw_input.text())
      self.callPark = GetCallPark(service.service)
      self.main_win.OutputListWidget.clear()
      self.callPark.callParkList
      for callPark in self.callPark.callParkList:
         singeLine = callPark['pattern'] + ' - ' + callPark['description']
         QListWidgetItem(singeLine, self.main_win.OutputListWidget)
                    
   def list_shared_lines(self):
      service = InitialZeep(self.main_win.cucm_ip_input.text(), self.main_win.cucm_uname_input.text(), self.main_win.cucm_pw_input.text())
      
      self.main_win.progressBar.show()
      self.worker = GetSharedLines(service.service)
      self.worker.api_error.connect(self.return_error)
      self.worker.finished.connect(self.update_shared_lines_table)
      self.worker.start()

   def update_shared_lines_table(self, list):
      self.main_win.OutputListWidget.clear()
      if len(list) > 0:
         for item in list:
            QListWidgetItem(item, self.main_win.OutputListWidget)
      else:
         QListWidgetItem('No Items', self.main_win.OutputListWidget)
      self.main_win.progressBar.hide()
      
   def list_meetmes(self):
      service = InitialZeep(self.main_win.cucm_ip_input.text(), self.main_win.cucm_uname_input.text(), self.main_win.cucm_pw_input.text())
      self.meetMe = GetMeetMe(service.service)
      self.main_win.OutputListWidget.clear()
      for meetMePattern in self.meetMe.meetMeList:
         singeLine = meetMePattern['pattern'] + '\t' + meetMePattern['description']+ ' \t ' + meetMePattern['securityLevel']
         QListWidgetItem(singeLine, self.main_win.OutputListWidget)
      self.main_win.statusbar.clearMessage()
      
   def list_facs(self):
      service = InitialZeep(self.main_win.cucm_ip_input.text(), self.main_win.cucm_uname_input.text(), self.main_win.cucm_pw_input.text())
      self.fac = GetFAC(service.service)
      self.main_win.OutputListWidget.clear()
      self.fac.facList
      for fac in self.fac.facList:
         singeLine = fac['name'] + ' - ' + fac['code']
         QListWidgetItem(singeLine, self.main_win.OutputListWidget)
      
   def get_cuc_version(self):
      creds = {'username': self.main_win.cuc_uname_input.text(), 'ip': self.main_win.cuc_ip_input.text(), 'password': self.main_win.cuc_pw_input.text()}
      res = get_cuc_version(creds)
      if (res):
         self.main_win.cuc_ver_label.setText(res['version'])
   
   def get_cer_version(self):
      creds = {'username': self.main_win.cer_uname_input.text(), 'ip': self.main_win.cer_ip_input.text(), 'password': self.main_win.cer_pw_input.text()}
      version = get_cer_version(creds)
      self.main_win.cuc_ver_label.setText(version['version'])
         
   def list_vm_users(self):
      creds = {'username': self.main_win.cuc_uname_input.text(), 'ip': self.main_win.cuc_ip_input.text(), 'password': self.main_win.cuc_pw_input.text()}
      
      self.main_win.progressBar.show()
      self.thread = QThread()
      self.worker = VoicemailUserWorker(creds)
      self.worker.api_error.connect(self.return_error)
      self.worker.finished_download.connect(self.update_voicemailusers_table)
      self.worker.start()
        
   def update_voicemailusers_table(self, data):
      model = VoicemailUserModel(data)
      self.main_win.progressBar.hide()
      self.vm_user_view = VoicemailUserView(model)    
   
   def list_call_handlers(self):
      creds = {'username': self.main_win.cuc_uname_input.text(), 'ip': self.main_win.cuc_ip_input.text(), 'password': self.main_win.cuc_pw_input.text()}
      
      self.main_win.progressBar.show()
      self.thread = QThread()
      self.worker = CallHandlerWorker(creds)
      self.worker.api_error.connect(self.return_error)
      self.worker.finished_download.connect(self.update_callhandler_table)
      self.worker.start()
        
   def update_callhandler_table(self, data):
      model = CallHandlerModel(data)
      self.main_win.progressBar.hide()
      self.phone_view = CallHandlerView(model)    

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