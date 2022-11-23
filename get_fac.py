"""
    GetFAC Class is used to query all Fored Authorization Codes configured in CUCM
    Iterate through the CallPark response and create a dictionary of list with the Name and Code.
    Name and Code are both mandatory fields in CUCM
"""
from error_dialog import ErrorDialog
import logging

class GetFAC:
    def __init__(self, service):
        self._service = service
        self.facList = []

        self.get_fac()
        
    def get_fac(self):

        try:
            listFacInfoRes = self._service.listFacInfo( searchCriteria = { 'name': '%' }, returnedTags = {} )
            
            if listFacInfoRes['return'] is not None:
                for facList in listFacInfoRes['return']['facInfo']:
                    getFacInfoRes = self._service.getFacInfo( uuid = facList['uuid'] )
                    self.facList.append({
                        'name': getFacInfoRes['return']['facInfo']['name'],
                        'code': getFacInfoRes['return']['facInfo']['code']
                        })
            else:
                self.facList = [{'name': 'No FAC', 'code': ''}] #Create Empty List if no FACs are configured in CUCM

        except BaseException as be:
            logging.warning('get_fac.py %s ', be)
            ErrorDialog(be)
