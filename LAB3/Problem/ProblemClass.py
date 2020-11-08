class Problem:
    def __init__(self, problemFile):
        self.__particleLength = None
        self.__connections = None
        self.__nrSteps = None
        self.loadProblem(problemFile)

    def getParticleLength(self):
        return self.__particleLength

    def getConnections(self):
        return self.__connections

    def getNrSteps(self):
        return self.__nrSteps

    def loadProblem(self, problemFile):
        f = open(problemFile, "r")
        self.__particleLength = int(f.readline().strip())
        connections = {}
        for i in range(self.__particleLength):
            #get the list of connections
            conn = []
            line = f.readline().strip()
            attrs = line.split(" ")
            for c in attrs:
                conn.append(int(c))
            connections[i] = conn
        self.__connections = connections
        self.__nrSteps = int(f.readline().strip())