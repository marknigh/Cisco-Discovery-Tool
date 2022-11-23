'''
    Class to retrieve all Meet-Me numbers configured in CUCM.
    
    Pattern and Security Level are mandatory fields in CUCM. Description is optional and if blank Zeep
    returns a NoneType.

'''

from error_dialog import ErrorDialog
import logging
from zeep import xsd
from zeep.helpers import serialize_object
class GetMeetMe:
    def __init__(self, service):
        self._service = service
        self.meetMeList = []

        self.get_meetme()
        
    def get_meetme(self):

        try:
            listMeetMeResponse = self._service.listMeetMe( searchCriteria = {'pattern': '%'}, returnedTags = {} )
            
            if listMeetMeResponse['return'] is not None:
                for meetMe in listMeetMeResponse['return']['meetMe']:
                    getMeetMeRes = self._service.getMeetMe( uuid = meetMe['uuid'] )

                    meetMe_dict = {
                        'pattern': getMeetMeRes['return']['meetMe']['pattern'],
                        'securityLevel': getMeetMeRes['return']['meetMe']['minimumSecurityLevel']
                        }
                    
                    if getMeetMeRes['return']['meetMe']['description'] is not None:
                        meetMe_dict['description'] = getMeetMeRes['return']['meetMe']['description']
                    else:
                        meetMe_dict['description'] = ''
                    
                    self.meetMeList.append(meetMe_dict)
            
            else:
                # Create Empty List if no Meet-Mes are configured
                self.meetMeList = [{'pattern': 'No MeetMe Numbers', 'description': '', 'securityLevel': ''}] 

        except BaseException as be:
            logging.warning('get_meetme %s ', be)
            ErrorDialog(be)
