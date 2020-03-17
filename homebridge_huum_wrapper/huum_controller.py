import requests

from homebridge_huum_wrapper.models import HuumResponse, WebThermostatStatusResponse, door


class Huum(object):
    root_url = None
    username = None
    password = None
    temperature = 40
    max_temp = 110
    min_temp = 40

    def __init__(self, username, password, root_url, start_temp=40):
        self.username = username
        self.password = password
        self.root_url = root_url
        self.start_temp = start_temp

    def status(self):
        res = requests.get(self.root_url.format("status"),
                           auth=(self.username, self.password))
        if res:
            return WebThermostatStatusResponse(**res.json())
        return WebThermostatStatusResponse(status="unknown")

    def start(self, targetTemperature=40):
        if targetTemperature not in range(self.min_temp,self.max_temp):
            return HuumResponse(status="error", details="{} is out of range".format(targetTemperature))
        status = self.status()
        # Safety measure. If door is open then ignore.
        if not status.door:
            return HuumResponse(status="error", details=door.get(status.door))
        res = requests.post(self.root_url.format("start"),
                            data=dict(targetTemperature=targetTemperature),
                            auth=(self.username, self.password))
        if res:
            return HuumResponse(**res.json())
        return HuumResponse(status="unknown")

    def stop(self):
        res = requests.post(self.root_url.format("stop"), auth=(self.username, self.password))
        if res:
            return HuumResponse(**res.json())
        return HuumResponse(status="unknown")
