'''
 SOAP API call to CUCM to retrieve all devices configured (registered or not) in CUCM. This file consist of the MVC (Model/ViewControll)
 data model for PyQt5.  
 
'''
from error_dialog import ErrorDialog
from PyQt5.QtCore import QObject, QAbstractTableModel, Qt, pyqtSignal, QThread
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from list_phone_view import Ui_MainWindow
import logging

class PhoneWorker(QThread):
    finished_data = pyqtSignal(list)
    api_error = pyqtSignal(object)
    
    def __init__(self, service, parent=None):
        super().__init__()
        self.data = []
        self._service = service
        
    def run(self):

        try:
            ListPhoneRes = self._service.listPhone( searchCriteria = { 'name': '%' }, returnedTags = {} )
            for i in ListPhoneRes['return']['phone']:
                getPhoneRes = self._service.getPhone( uuid = i['uuid'] )
            
                phone_dict = {
                        'name': getPhoneRes['return']['phone']['name'],
                        'description': getPhoneRes['return']['phone']['description'],
                        'model': getPhoneRes['return']['phone']['model']
                        }

                line_string = ''
                for line in getPhoneRes['return']['phone']['lines']['line']:
                    line_string += line['dirn']['pattern'] + ', '
                line_string = line_string[:-2]
                phone_dict['lines'] = line_string
                self.data.append(phone_dict)

            self.finished_data.emit(self.data)
                
        except BaseException as be:
            logging.warning('get_phones.py %s ', be)
            self.api_error.emit(be)

class PhoneListView(QObject): 
    def __init__(self, model):
        super().__init__()
        self.window = QMainWindow()
        self.phone_win = Ui_MainWindow()
        self.phone_win.setupUi(self.window)
        self.window.show()
        self._data = model.data
        self.phone_win.phone_tableView.setModel(model)
        self.phone_win.export_btn.clicked.connect(self.export_to_file)
    
    def export_to_file(self):
        self.clean_data()
        folderpath = QFileDialog.getSaveFileName()
        f = open(folderpath[0], 'w')
        f.write('name' + ',' + 'description' + ',' + 'model' + ',' + 'lines' + '\n')
        for item in self._data:
            #build string to export
            export_string = item['name'] + ',' + item['description'] + ',' + item['model'] + ',' + item['lines'] + '\n'
            f.write(export_string)

    def clean_data(self):
        for item in self._data:
            for key in item:
                if item[key] is None:
                    item[key] = ''

class PhoneModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.headers = ['name', 'description', 'model', 'lines']
        
    def rowCount(self, n):
        return len(self.data)
    
    def columnCount(self, n):
        return 4

    def data(self,index,role):
        if role == Qt.DisplayRole:
            column = index.column()
            return self.data[index.row()][self.headers[column]]