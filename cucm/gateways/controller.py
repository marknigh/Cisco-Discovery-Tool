# MVC design pattern for call park

from .get_gateways import GetGateways
from .build_gateway_tree import BuildGatewayWindow

def list_gateways(main_window):
    gatewayList = GetGateways(main_window.service)
    return BuildGatewayWindow(gatewayList.gatewayList)
    

