from random import randint
from random import shuffle

from Particle.ParticleClass import Particle


class Swarm:
    def __init__(self, populationLength, sizeOfNeighbourhood, problem):
        self.__allParticles = [Particle(problem) for i in range(populationLength)]
        self.__populationLength = populationLength
        self.__neighbourhoods = self.computeNeighbours(sizeOfNeighbourhood)

    def getAllParticles(self):
        return self.__allParticles

    def getPopulationLength(self):
        return self.__populationLength

    def getNeighbourhoods(self):
        return self.__neighbourhoods

    def getParticleFromPos(self, pos):
        return self.__allParticles[pos]

    def computeNeighbours(self, sizeOfNeighbourhood):
        if sizeOfNeighbourhood > self.__populationLength:
            sizeOfNeighbourhood = self.__populationLength

        # Attention if nSize==len(pop) this selection is not a propper one
        # use a different approach (like surfle to form a permutation)
        neighbours = []
        if sizeOfNeighbourhood == self.__populationLength:
            for i in range(self.__populationLength):
                localNeighbor = [j for j in range(self.__populationLength)]
                localNeighbor.remove(i)
                shuffle(localNeighbor)
                neighbours.append(localNeighbor.copy())
            return neighbours
        else:
            for i in range(self.__populationLength):
                localNeighbor = []
                for j in range(sizeOfNeighbourhood):
                    oneNeighbour = randint(0, self.__populationLength - 1)
                    while (oneNeighbour in localNeighbor):
                        oneNeighbour = randint(0, self.__populationLength - 1)
                    localNeighbor.append(oneNeighbour)
                neighbours.append(localNeighbor.copy())
            return neighbours

    def getBestNeighbour(self, posOfParticle):
        bestNeighbour = 0
        for i in range(1, len(self.__neighbourhoods[posOfParticle])):
            if (self.__allParticles[bestNeighbour].getFitness() >
                    self.__allParticles[self.__neighbourhoods[posOfParticle][i]].getFitness()):
                bestNeighbour = self.__neighbourhoods[posOfParticle][i]
        return bestNeighbour

    def getBestParticles(self):
        bestParticleFitness = self.__allParticles[0].getFitness()
        for i in range(1, self.__populationLength):
            if self.__allParticles[i].getFitness() < bestParticleFitness:
                bestParticleFitness = self.__allParticles[i].getFitness()
        bestParticles = []
        for i in range(self.__populationLength):
            if self.__allParticles[i].getFitness() == bestParticleFitness:
                bestParticles.append(i)

        return bestParticles
