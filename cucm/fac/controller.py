"""
    
"""
from utilities.error_dialog import ErrorDialog
import logging
from .view import FACListView
from .model import FACModel
       
def get_fac(self):
    facList = []
    try:
        listFacInfoRes = self.service.service.listFacInfo( searchCriteria = { 'name': '%' }, returnedTags = {} )
        
        if listFacInfoRes['return'] is not None:
            for fac in listFacInfoRes['return']['facInfo']:
                getFacInfoRes = self.service.service.getFacInfo( uuid = fac['uuid'] )
                facList.append({
                    'name': getFacInfoRes['return']['facInfo']['name'],
                    'code': getFacInfoRes['return']['facInfo']['code']
                    })
        else:
            facList = [{'name': 'No FAC', 'code': ''}] #Create Empty List if no FACs are configured in CUCM

        model = FACModel(facList)
        return FACListView(model)

    except BaseException as be:
        logging.warning('get_fac.py %s ', be)
        ErrorDialog(be)
