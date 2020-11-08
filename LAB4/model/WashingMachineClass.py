class WashingMachine:
    def __init__(self):
        self.__texture = None
        self.__capacity = None
        self.__cycleType = None

    def getTexture(self):
        return self.__texture

    def setTexture(self, value):
        self.__texture = value

    def getCapacity(self):
        return self.__capacity

    def setCapacity(self, value):
        self.__capacity = value

    def getCycleType(self):
        return self.__cycleType

    def setCycleType(self, value):
        self.__cycleType = value

    def __str__(self):
        return "{" + str(self.__texture) + " " + str(self.__capacity) + " " + str(self.__cycleType) + "}"
