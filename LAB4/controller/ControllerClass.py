from model.WashingMachineClass import WashingMachine


class Controller:
    def __init__(self):
        self.__washingMachine = WashingMachine()
        self.__textureDict = {}
        self.__capacityDict = {}
        self.__cycleDict = {}
        self.__tableList = []
        self.__setDicts()
        print(self)

    def computeTriangle(self, x, a, b, c):
        if b - a != 0 and c - b != 0:
            return max(0, min((x - a) / (b - a), 1, (c - x) / (c - b)))
        if b - a == 0 and c - b == 0:
            return 1
        if b - a == 0:
            return max(0, min(1, (c - x) / (c - b)))
        if c - b == 0:
            return max(0, min((x - a) / (b - a), 1))

    def computeTrapez(self, x, a, b, c, d):
        if b - a != 0 and d - c != 0:
            return max(0, min((x - a) / (b - a), 1, (d - x) / (d - c)))
        if b - a == 0 and d - c == 0:
            return 1
        if b - a == 0:
            return max(0, min(1, (d - x) / (d - c)))
        if d - c == 0:
            return max(0, min((x - a) / (b - a), 1))

    def determineCycleType(self, texture, capacity):
        self.__washingMachine.setTexture(texture)
        self.__washingMachine.setCapacity(capacity)
        textureList = self.getTextureList()
        capacityList = self.getCapacityList()
        filledTable = self.fillTable(textureList, capacityList)
        maxTable = self.getMaxTable(filledTable)
        self.__setCycle(maxTable)

        print(textureList)
        print(capacityList)
        print(filledTable)
        print(maxTable)

    def __setDicts(self):
        f = open("problem.in", "r")
        for i in range(4):
            line = f.readline().strip()
            attrs = line.split(" ")
            values = []
            for i in range(1, len(attrs)):
                values.append(float(attrs[i]))
            self.__textureDict[attrs[0]] = values
        for i in range(3):
            line = f.readline().strip()
            attrs = line.split(" ")
            values = []
            for i in range(1, len(attrs)):
                values.append(float(attrs[i]))
            self.__capacityDict[attrs[0]] = values
        for i in range(4):
            line = f.readline().strip()
            attrs = line.split(" ")
            values = []
            for i in range(1, len(attrs)):
                values.append(float(attrs[i]))
            self.__cycleDict[attrs[0]] = values
        self.__tableList = f.readline().strip().split(" ")
        f.close()

    def __str__(self):
        return "washing machine " + str(self.__washingMachine) + "\n" + "textureDict: " + str(
            self.__textureDict) + "\n" + "capacityDict: " + str(self.__capacityDict) + "\n" + "cycleDict: " + str(
            self.__cycleDict) + "\n" + "tableList: " + str(self.__tableList) + "\n"

    def getTextureList(self):
        textureList = []
        for key in self.__textureDict.keys():
            if len(self.__textureDict[key]) == 3:
                textureList.append(self.computeTriangle(self.__washingMachine.getTexture(), self.__textureDict[key][0],
                                                        self.__textureDict[key][1],
                                                        self.__textureDict[key][2]))
            else:
                textureList.append(self.computeTrapez(self.__washingMachine.getTexture(), self.__textureDict[key][0],
                                                      self.__textureDict[key][1],
                                                      self.__textureDict[key][2], self.__textureDict[key][3]))
        return textureList

    def getCapacityList(self):
        capacityList = []
        for key in self.__capacityDict.keys():
            if len(self.__capacityDict[key]) == 3:
                capacityList.append(
                    self.computeTriangle(self.__washingMachine.getCapacity(), self.__capacityDict[key][0],
                                         self.__capacityDict[key][1],
                                         self.__capacityDict[key][2]))
            else:
                capacityList.append(
                    self.computeTrapez(self.__washingMachine.getCapacity(), self.__capacityDict[key][0],
                                       self.__capacityDict[key][1],
                                       self.__capacityDict[key][2], self.__capacityDict[key][3]))
        return capacityList

    def fillTable(self, textureList, capacityList):
        tableContor = -1
        filledTable = []
        for i in textureList:
            for j in capacityList:
                tableContor += 1
                filledTable.append((self.__tableList[tableContor], min(i, j)))
        return filledTable

    def getMaxTable(self, filledTable):
        maxTable = {}
        for key in self.__cycleDict.keys():
            maxTable[key] = 0
        for tuple in filledTable:
            if tuple[1] > maxTable[tuple[0]]:
                maxTable[tuple[0]] = tuple[1]
        return maxTable

    def getCurrentCycleType(self):
        return self.__washingMachine.getCycleType()

    def __setCycle(self, maxTable):
        s = sum(maxTable.values())
        ponder = 0
        points = []
        for value in self.__cycleDict.values():
            points.append(value[1])
        print(points)
        i = -1
        for value in maxTable.values():
            i += 1
            ponder += value * points[i]

        self.__washingMachine.setCycleType(ponder/s)