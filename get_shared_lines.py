"""
Get Shared Lines. Use the listPhone query to return all phones. interate over the phones and place each line of the phone within a list.
Use pyDash and find all duplicates. Return duplicates to Main Window class to update table widget via pyqtSignal. 

"""
from PyQt5.QtCore import pyqtSignal, QThread
from pydash import duplicates
import logging

class GetSharedLines(QThread):
    finished = pyqtSignal(list)
    api_error = pyqtSignal(object)
        
    def __init__(self, service):
        super(GetSharedLines, self).__init__()
        self._service = service
        self.sharedLinesList = []
        
    def run(self):
        try:
            ListPhoneRes = self._service.listPhone( searchCriteria = { 'name': '%' }, returnedTags = {} )
            for phone in ListPhoneRes['return']['phone']:
            
                try:
                    getPhoneRes = self._service.getPhone( uuid = phone['uuid'] )

                    for line in getPhoneRes['return']['phone']['lines']['line']:
                        self.sharedLinesList.append(line['dirn']['pattern'])
                                           
                except BaseException as be:
                    logging.warning('get_shared_lines %s', be)
                    self.api_error.emit(be)

            self.sharedLinesList = duplicates(self.sharedLinesList) 

            # if (len(self.sharedLinesList) > 0):
            #     for sharedLine in self.sharedLinesList:
            #         QListWidgetItem(sharedLine, self._main_win.OutputListWidget)
            # else:
            #     QListWidgetItem('No Shared Lines', self.main_win.OutputListWidget)
            
            self.finished.emit(self.sharedLinesList)

        except BaseException as be:
            logging.warning('get_shared_lines %s', be)
            self.api_error.emit(be)
