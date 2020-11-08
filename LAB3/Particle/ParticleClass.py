from random import randint


class Particle:
    def __init__(self, problem):
        self.__problem = problem
        self.__position = [randint(0,1) for i in range(problem.getParticleLength())]
        self.__velocity = [0 for i in range(problem.getParticleLength())]
        self.__fitness = None
        self.evaluate()
        self.__bestPosition = self.__position.copy()
        self.__bestFitness = self.__fitness

    def evaluate(self):
        self.__fitness = self.fit(self.__position)

    def fit(self, position):
        nrSteps = self.__problem.getNrSteps()
        infected = []
        #first step
        for i in range(len(self.__position)):
            if self.__position[i] == 1:
                infected.append(i)
        recentlyInfected = infected.copy()
        #rest of steps in order to see how many we can infect
        for i in range(nrSteps-1):
            #see who we can infect starting from the recently infected guys
            newRecentlyInfected = []
            for guyInfected in recentlyInfected:
                connectionsOfGuyInfected = self.__problem.getConnections()[guyInfected].copy()
                for connection in connectionsOfGuyInfected:
                    if connection not in infected:
                        newRecentlyInfected.append(connection)
            #now we update the guys we have just infected
            recentlyInfected = newRecentlyInfected.copy()
            #and add them to the infected list
            infected = infected + recentlyInfected.copy()
        infected = list(dict.fromkeys(infected))
        if len(infected) < len(self.__position):
            return len(self.__position) - len(infected)
        else:
            return -(len(self.__position) - self.__position.count(1))



    def getPosition(self):
        return self.__position

    def setPosition(self, newPosition):
        self.__position = newPosition.copy()
        # automatic evaluation of particle's fitness
        self.evaluate()
        # automatic update of particle's memory
        if (self.__fitness < self.__bestFitness):
            self.__bestPosition = self.__position
            self.__bestFitness = self.__fitness

    def getVelocity(self):
        return self.__velocity

    def getFitness(self):
        return self.__fitness

    def getBestPosition(self):
        return self.__bestPosition

    def getBestFitness(self):
        return self.__bestFitness
