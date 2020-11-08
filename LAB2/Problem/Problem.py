class Problem:
    def __init__(self, file_name):
        self.__maximumWeight = None
        self.__jewelryCollection = []
        self.__collectionSize = None
        self.loadData(file_name)

    def loadData(self, file_name):
        f = open(file_name, "r")
        self.__maximumWeight = int(f.readline().strip())
        self.__collectionSize = int(f.readline().strip())
        for i in range(self.__collectionSize):
            # value,price pairs
            line = f.readline().strip()
            attrs = line.split(" ")
            self.__jewelryCollection.append([int(attrs[0]), int(attrs[1])])
        f.close()

    def getMaximumWeight(self):
        return self.__maximumWeight

    def getJewelryCollection(self):
        return self.__jewelryCollection

    def getCollectionSize(self):
        return self.__collectionSize
