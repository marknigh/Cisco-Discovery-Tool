'''
    This module is retrieve all SIP Trunks configured in CUCM and view the name, description and destination IPs.
'''

from zeep import xsd
import logging
from error_dialog import ErrorDialog

class GetTrunks:
    def __init__(self, service):
        self._service = service
        self.sipTrunkList = []
        
        self.get_sipTrunks()
        
    def get_sipTrunks(self):

        try:
            listSipTrunkResponse = self._service.listSipTrunk( searchCriteria = { 'name': '%' }, returnedTags = {'uuid': xsd.Nil, 'name': xsd.Nil, 'description': xsd.Nil, 'product': xsd.Nil } )
            for trunk in listSipTrunkResponse['return']['sipTrunk']:
                trunk_dict = {
                        'name': trunk['name'],
                        'model': trunk['product'],
                        'destinations': []
                        }               
                if trunk['description'] is not None:
                    trunk_dict['description'] = trunk_dict['return']['meetMe']['description']
                else:
                    trunk_dict['description'] = ''

                getSipTrunkResponse = self._service.getSipTrunk( uuid = trunk['uuid'], returnedTags = { 'name': xsd.Nil, 'description': xsd.Nil, 'product': xsd.Nil, 'destinations': { 'destination': { 'addressIpv4': '', 'addressIpv6': '', 'port': '', 'sortOrder': '' } } }  )
                for destination in getSipTrunkResponse['return']['sipTrunk']['destinations']['destination']:
                    destinations_dict = {'ipv4': destination['addressIpv4'], 'port': destination['port']}
                    
                    trunk_dict['destinations'].append(destinations_dict)
                               
                self.sipTrunkList.append(trunk_dict)
            
        except BaseException as be:
            logging.warning('get_trunks %s ', be)
            ErrorDialog(be)
