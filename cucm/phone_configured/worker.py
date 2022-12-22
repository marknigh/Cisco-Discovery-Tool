from PyQt5.QtCore import pyqtSignal, QThread
import logging

class PhoneWorker(QThread):
    finished_data = pyqtSignal(list)
    api_error = pyqtSignal(object)
    
    def __init__(self, service, parent=None):
        super(PhoneWorker, self).__init__()
        self.data = []
        self._service = service
        
    def run(self):

        try:
            ListPhoneRes = self._service.service.listPhone( searchCriteria = { 'name': '%' }, returnedTags = {} )
            for i in ListPhoneRes['return']['phone']:
                getPhoneRes = self._service.service.getPhone( uuid = i['uuid'] )
            
                phone_dict = {
                        'name': getPhoneRes['return']['phone']['name'],
                        'model': getPhoneRes['return']['phone']['model']
                        }

                if getPhoneRes['return']['phone']['description'] is None:
                    phone_dict['description'] = ''
                else:
                    phone_dict['description'] = getPhoneRes['return']['phone']['description']

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