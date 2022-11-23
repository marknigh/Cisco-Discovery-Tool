"""
 This Class is used to intialize the client and settings for the Zeep library.
 Other classes or functions will use the service (Zeep Client.create_service) ServiceProxy Object
"""

from zeep import Client, Settings
from zeep.transports import Transport

from requests import Session
from requests.auth import HTTPBasicAuth

WSDL_FILE = 'RISService70.wsdl'

class InitialRISZeep:
    def __init__(self, ip, username, password):
        self._ip = ip
        self._username = username
        self._password = password
        self.session = Session()
        self.session.verify = False
        self.session.auth = HTTPBasicAuth(self._username, self._password)
        self.transport = Transport(session = self.session, timeout = 5)
        self.settings = Settings( strict=False, xml_huge_tree=True )
        self.client = Client( wsdl=WSDL_FILE, settings = self.settings, transport = self.transport, plugins=[])
        self.service = self.client.create_service( '{http://schemas.cisco.com/ast/soap}RisBinding',
                                f'https://{self._ip}:8443/realtimeservice2/services/RISService70' )

