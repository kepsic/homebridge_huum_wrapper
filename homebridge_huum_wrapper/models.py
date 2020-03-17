statusCode = {
    230: "Sauna offline",
    231: "Online and heating",
    232: "Online but not heating"
}

states = {
    0:	"Off",
    1:	"Heat",
    2:	"Cool",
    3:	"Auto",
}

door = {
    True: "The door is closed",
    False: "The door is open and can't be started"
}

config = {
    1: "Shows that the controller is configured to use a light system",
    2: "Shows that the controller is configured to use a steamer system",
    3: "Shows that the controller is configured to use both the light and steamer system"
}

steamerError = {
    1: "The steamer is empty of water and needs to be refilled also no steamer start allowed"
}


class HuumResponse(object):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)


class HuumRequest(object):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)


class WebThermostatStatusResponse(object):
    targetHeatingCoolingState = None
    targetTemperature = None
    currentHeatingCoolingState = None
    currentTemperature = None
    currentRelativeHumidity = None
    coolingThresholdTemperature = None
    heatingThresholdTemperature = None

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
            if k == "temperature":
                self.currentTemperature = v
            elif k == "statusCode" and v == 231:
                self.targetHeatingCoolingState = 1
            elif k == "statusCode" and (v == 230 or v == 232):
                self.targetHeatingCoolingState = 0

