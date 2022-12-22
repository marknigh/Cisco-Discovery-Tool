'''
    Get all hunt groups configured in CUCM. Create tree data structure. 
'''

import logging
from utilities.error_dialog import ErrorDialog


class GetHuntGroups():
    def __init__(self, service):
        self._service = service
        self.tree_view = []
        self.get_list_pilot()

    def get_list_pilot(self):
        
        try:
            list_hunt_pilots = self._service.service.listHuntPilot( searchCriteria = { 'pattern': '%' }, returnedTags = {} )
            for pilot_list in list_hunt_pilots['return']['huntPilot']:
                pilot_details = self.get_pilot_details(pilot_list.uuid)
                
                hunt_list = self.get_hunt_list(pilot_details['return']['huntPilot']['huntListName'].uuid)
                tree_dict = {'pilot': pilot_details['return']['huntPilot'].pattern,
                             'description': pilot_details['return']['huntPilot'].description,
                             'hunt_list': hunt_list['return']['huntList'].name,
                             'hunt_list_members': []}
                
                for member in hunt_list['return']['huntList']['members']['member']:
                    member_dict = {'name': member['lineGroupName']['_value_1'],
                                    'line_members': []
                                    }
                    
                    line_group = self.get_hunt_members(member['lineGroupName']['uuid'])
                    if line_group['return']['lineGroup']['members'] is not None:
                        for member_pattern in line_group['return']['lineGroup']['members']['member']:
                            member_dict['line_members'].append({'pattern': member_pattern['directoryNumber']['pattern']})
                    tree_dict['hunt_list_members'].append(member_dict)
                self.tree_view.append(tree_dict)

        except BaseException as be:
            logging.warning('get_gateway_detail %s ', be)
            ErrorDialog(be)
    
    def get_pilot_details(self, uuid):
        try:
            pilot_detail = self._service.service.getHuntPilot( uuid = uuid )
            return pilot_detail
        
        except BaseException as be:
            logging.warning('get_pilot_details %s ', be)
            ErrorDialog(be)

    def get_hunt_list(self, uuid):
        try:
            hunt_list = self._service.service.getHuntList( uuid = uuid )
            return hunt_list
        
        except BaseException as be:
            logging.warning('get_hunt_list %s ', be)
            ErrorDialog(be)

    def get_hunt_members(self, uuid):
        try:
            line_group = self._service.service.getLineGroup( uuid = uuid )
            return line_group
        
        except BaseException as be:
            logging.warning('get_hunt_members %s ', be)
            ErrorDialog(be)
