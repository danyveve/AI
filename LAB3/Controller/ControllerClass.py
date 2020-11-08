from random import random
import math
from Problem.ProblemClass import Problem
from Swarm.SwarmClass import Swarm

import matplotlib.pyplot as plt

class Controller:
    def __init__(self, parameterFile, problemFile):
        self.__nrIterations = None
        self.__nrParticles = None
        self.__sizeOfNeighbourhood = None
        self.__w = None
        self.__c1 = None
        self.__c2 = None
        self.loadParameters(parameterFile)

        self.__problem = Problem(problemFile)
        self.__sizeOfParticle = self.__problem.getParticleLength()

        self.__swarm = Swarm(self.__nrParticles, self.__sizeOfNeighbourhood, self.__problem)

    def iteration(self, w):
        # determine the best neighbor for each particle
        bestNeighbours = []
        for i in range(self.__nrParticles):
            bestNeighbours.append(self.__swarm.getBestNeighbour(i))
        # update the velocity for each particle
        for i in range(self.__nrParticles):
            for j in range(self.__sizeOfParticle):
                newVelocity = w * self.__swarm.getParticleFromPos(i).getVelocity()[j]
                newVelocity = newVelocity + self.__c1 * random() * (self.__swarm.getParticleFromPos(bestNeighbours[i]).getPosition()[j]
                                                                    - self.__swarm.getParticleFromPos(i).getPosition()[j])
                newVelocity = newVelocity + self.__c2 * random() * (self.__swarm.getParticleFromPos(i).getBestPosition()[j]
                                                                    - self.__swarm.getParticleFromPos(i).getPosition()[j])
                self.__swarm.getParticleFromPos(i).getVelocity()[j] = newVelocity

        # update the pozition for each particle
        for i in range(self.__nrParticles):
            newPosition = []
            for j in range(self.__sizeOfParticle):
                #newPosition.append(pop[i].pozition[j] + pop[i].velocity[j])
                if(self.sigmoid(self.__swarm.getParticleFromPos(i).getVelocity()[j]) >= 0.5):
                    newPosition.append(1)
                else:
                    newPosition.append(0)
            self.__swarm.getParticleFromPos(i).setPosition(newPosition)



    def runAlg(self):
        for i in range (self.__nrIterations):
            self.iteration(self.__w / (i+1))

        self.printBestIndividual()

    @staticmethod
    def runStatistics():
        bestValuesObtained = []
        for i in range(30):
            bestFitness = Controller("statisticparameters.in", "problem1.in").__doOneStatisticRun()
            bestValuesObtained.append(bestFitness)
        # now we will compute the standard deviation and the mean
        s = sum(bestValuesObtained, 0)
        mean = s / len(bestValuesObtained)

        recompArray = []
        for val in bestValuesObtained:
            recompArray.append((val - mean) * (val - mean))
        s2 = sum(recompArray, 0)
        m2 = s2 / len(recompArray)
        standardDeviation = math.sqrt(m2)

        print("Statistics result: ")
        print(" Mean: " + str(mean))
        print(" Standard Deviation: " + str(standardDeviation))

        return Controller("statisticparameters.in", "problem1.in").__doOnePlot()

    def __doOneStatisticRun(self):
        for i in range (self.__nrIterations):
            self.iteration(self.__w / (i+1))
        #return the best
        best = 0
        for i in range(1, self.__nrParticles):
            # if (P[i].fitness < P[best].fitness):
            #   best = i
            if self.__swarm.getParticleFromPos(i).getFitness() < self.__swarm.getParticleFromPos(best).getFitness():
                best = i

        return self.__swarm.getParticleFromPos(best).getFitness()


    def __doOnePlot(self):
        values = []
        for i in range (self.__nrIterations):
            self.iteration(self.__w / (i+1))
            evaluation = [p.getFitness() for p in self.__swarm.getAllParticles()]
            mean = sum(evaluation) / len(evaluation)
            values.append(mean)
        iterations = [i for i in range(1, 1001)]
        plt.plot(iterations, values)
        plt.xlabel("Iterations")
        plt.ylabel("Fitness")
        plt.show()

    def loadParameters(self, parameterFile):
        f = open(parameterFile, "r")
        self.__nrIterations = int(f.readline().strip())
        self.__nrParticles = int(f.readline().strip())
        self.__sizeOfNeighbourhood = int(f.readline().strip())
        self.__w = float(f.readline().strip())
        self.__c1 = float(f.readline().strip())
        self.__c2 = float(f.readline().strip())

    @staticmethod
    def sigmoid(x):
        return 1 / (1 + math.exp(-x))

    def printBestIndividual(self):
        # print the best individual
        best = 0
        for i in range(1, self.__nrParticles):
            #if (P[i].fitness < P[best].fitness):
             #   best = i
            if self.__swarm.getParticleFromPos(i).getFitness() < self.__swarm.getParticleFromPos(best).getFitness():
                best = i


        fitnessOptim = self.__swarm.getParticleFromPos(best).getFitness()
        individualOptim = self.__swarm.getParticleFromPos(best).getPosition()
        computers = []
        for i in range(self.__sizeOfParticle):
            if(individualOptim[i] == 1):
                computers.append(i)
        print("The minimum computers needed to spread the infection are: ")
        print(computers)
        print("With fitness: ")
        print(fitnessOptim)


