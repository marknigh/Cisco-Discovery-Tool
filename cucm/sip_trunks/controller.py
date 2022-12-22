# MVC design pattern for call park

from .get_trunks import GetTrunks
from .model import SipTrunkModel
from .view import SipTrunkListView

def list_siptrunks(main_window):
    sip_trunks = GetTrunks(main_window.service)
    model = SipTrunkModel(sip_trunks.sipTrunkList)
    return SipTrunkListView(model)