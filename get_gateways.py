'''
    Get Gateways from CUCM
'''
import logging
from error_dialog import ErrorDialog

class GetGateways:
    def __init__(self, service):
        self._service = service
        self.gatewayList = []
        self.get_gateways()
        
    def get_gateways(self):

        try:
            listGatewayRes = self._service.listGateway( searchCriteria = { 'domainName': '%' }, returnedTags = {} )
            if listGatewayRes['return'] is not None:
                for gateway in listGatewayRes['return']['gateway']:
                    self.get_gateway_details(gateway['uuid'])
                
        except BaseException as be:
            logging.warning('get_gateways %s ', be)
            open = ErrorDialog(be)
            open.exec()
            
    def get_gateway_details(self, gateway_uuid):
           
        try:
            gateway_dict = {}
            getGatewayRes = self._service.getGateway( uuid = gateway_uuid )
            gateway_dict = {
                    'name': getGatewayRes['return']['gateway']['domainName'],
                    'uuid': getGatewayRes['return']['gateway']['uuid'],
                    'description': getGatewayRes['return']['gateway']['description'],
                    'model': getGatewayRes['return']['gateway']['product'],
                    'protocol': getGatewayRes['return']['gateway']['protocol'],
                    'units': []
                    }

            for gatewayUnits in getGatewayRes['return']['gateway']['units']['unit']:
                unit_dict = {'index': gatewayUnits['index'], 'product': gatewayUnits['product'], 'subunits': []}
                endpoint_dict = self.get_endpoints(gateway_uuid, unit_dict['index'])
                unit_dict['endpoints'] = endpoint_dict
                
                for subU in gatewayUnits['subunits']['subunit']:
                    unit_dict['subunits'].append({'product': subU['product']})
                    
                gateway_dict['units'].append(unit_dict)
            
            # endpoint_dict = self.get_endpoints(gateway_uuid)
            # gateway_dict['endpoints'].append(endpoint_dict) 
            
            self.gatewayList.append(gateway_dict)
            
        except BaseException as be:
            logging.warning('get_gateway_detail %s ', be)
            open = ErrorDialog(be)
            open.exec()
            
    def get_endpoints(self, phone_uuid, index):
        strip_char = phone_uuid.replace('{', '').replace('}', '').lower()
        sql = f'''select * from mgcpdevicemember where fkmgcp="{strip_char}" and slot="{index}"'''
        executeSQLRes = self._service.executeSQLQuery( sql )
        endpoint_dict = []
        for rowXml in executeSQLRes['return']['row']:
            for row in rowXml:
                if row.tag == 'fkdevice':
                    getPhoneRes = self._service.getPhone( uuid = row.text )
                    if getPhoneRes['return']['phone']['lines'] is not None:
                        for line in getPhoneRes['return']['phone']['lines']['line']:
                            endpoint_dict.append({
                                'pattern': line['dirn']['pattern']
                            })
        return endpoint_dict