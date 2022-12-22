# MVC design pattern for call park

from .get_callpark import GetCallPark
from .model import CallParkModel
from .view import CallParkListView

def list_callparks(main_window):
    callPark = GetCallPark(main_window.service)
    model = CallParkModel(callPark.callParkList)
    return CallParkListView(model)