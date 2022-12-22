
import logging
from utilities.error_dialog import ErrorDialog
from .model import MeetMeModel
from .view import MeetMeListView

def list_meetmes(main_window):
    meetMeList = []
    try:
        listMeetMeResponse = main_window.service.service.listMeetMe( searchCriteria = {'pattern': '%'}, returnedTags = {} )
        
        if listMeetMeResponse['return'] is not None:
            for meetMe in listMeetMeResponse['return']['meetMe']:
                getMeetMeRes = main_window.service.service.getMeetMe( uuid = meetMe['uuid'] )

                meetMe_dict = {
                    'pattern': getMeetMeRes['return']['meetMe']['pattern'],
                    'securityLevel': getMeetMeRes['return']['meetMe']['minimumSecurityLevel']
                    }
                
                if getMeetMeRes['return']['meetMe']['description'] is not None:
                    meetMe_dict['description'] = getMeetMeRes['return']['meetMe']['description']
                else:
                    meetMe_dict['description'] = ''
                
                meetMeList.append(meetMe_dict)
        
        else:
            # Create Empty List if no Meet-Mes are configured
            meetMeList = [{'pattern': 'No MeetMe Numbers', 'description': '', 'securityLevel': ''}] 
        
        model = MeetMeModel(meetMeList)
        return MeetMeListView(model)
    
    except BaseException as be:
        logging.warning('get_meetme %s ', be)
        ErrorDialog(be)
        