""" Cornice services.
"""
from cornice import Service

from .huum_controller import Huum


def huum_controller(request):
    settings = request.registry.settings
    huum_username = settings.get("huum.username")
    huum_password = settings.get("huum.password")
    huum_url = settings.get("huum.api_url")
    start_temp = settings.get("huum.start_temp")
    return Huum(huum_username, huum_password, huum_url, int(start_temp))


state = Service(name='targetHeatingCoolingState',
                path='/targetHeatingCoolingState/{state}',
                description="HomeBridge set state")
status = Service(name='status',
                 path='/status',
                 description="HomeBridge status")

targetTemperature = Service(name='targetTemperature',
                            path='/targetTemperature/{temperature}',
                            description="HomeBridge targetTemperature")

targetRelativeHumidity = Service(name='targetRelativeHumidity',
                                 path='/targetRelativeHumidity/{targetRelativeHumidity}',
                                 description="HomeBridge targetRelativeHumidity")

last_target = 0

@state.get()
def set_state(request):
    global last_target
    state = request.matchdict.get("state")
    status = {}
    if state:
        state = int(state)
        controller = huum_controller(request)
        if state == 0:
            last_target = controller.status().targetTemperature
            status = controller.stop().__dict__
        elif state == 1 or state == 3:
            status = controller.start(last_target or controller.start_temp).__dict__
    return status


@status.get()
def get_status(request):
    global last_target
    controller = huum_controller(request).status()
    last_target = controller.targetTemperature
    return controller.__dict__


@targetTemperature.get()
def set_targetTemperature(request):
    global last_target
    _targetTemperature = request.matchdict.get("temperature")
    status = {}
    if _targetTemperature:
        _targetTemperature = int(_targetTemperature)
        status = huum_controller(request).start(targetTemperature=_targetTemperature)
        last_target = status.targetTemperature
        return status.__dict__
    return status


@targetRelativeHumidity.get()
def set_targetRelativeHumidity(request):
    return {"error": "Not implemented"}
