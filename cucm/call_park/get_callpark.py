"""
GetCallPark Class is used to query all CallParks configured in CUCM
Iterate through the CallPark response and create a dictionary of list with the Pattern and Description

"""

from utilities.error_dialog import ErrorDialog
import logging

class GetCallPark:
    def __init__(self, service):
        self.callParkList = []
        self.service = service
        self.get_callpark()
        
    def get_callpark(self):

        try:
            listCallParkRes = self.service.service.listCallPark( searchCriteria = { 'pattern': '%' }, returnedTags = {} )
            
            if listCallParkRes['return'] is not None:
                
                for call_park in listCallParkRes['return']['callPark']:
                    getCallParkRes = self.service.service.getCallPark( uuid = call_park['uuid'] )
                    self.callParkList.append({
                        'pattern': getCallParkRes['return']['callPark']['pattern'],
                        'description': getCallParkRes['return']['callPark']['description']
                        })
            
            else:
                self.callParkList = [{'pattern': 'No Call Parks', 'description': ''}] #Create Empty List if no Call Parks are configured
        
        except BaseException as be:
            logging.warning('get_callpark.py %s ', be)
            ErrorDialog(be)
