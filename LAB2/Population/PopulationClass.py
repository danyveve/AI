from Individ.IndividClass import Individual
from random import randint, random


class Population:
    def __init__(self, populationSize, individualSize):
        self.__populationSize = populationSize
        self.__individualsList = [Individual(individualSize) for i in range(0, populationSize)]

    def evaluate(self, problem):
        evaluation = []
        for i in range(self.__populationSize):
            evaluation.append([i, self.__individualsList[i].fitness(problem)])
        return evaluation

    def selectParents(self):
        p1 = randint(0, self.__populationSize - 1)  # p1=randint(0,  self.__populationSize - 2)
        p2 = randint(0, self.__populationSize - 1)  # p2 = randint(p1+1, self.__populationSize - 1)
        while (p2 != p1):
            p2 = randint(0, self.__populationSize - 1)

        return self.__individualsList[p1], self.__individualsList[p2]

    def selectSurvivor(self, child, problem):
        # child will replace the worst guy in the population
        evaluation = self.evaluate(problem)
        evaluation = sorted(evaluation, key=lambda x: x[1])
        posOfWorstGuy = evaluation[0][0]
        self.__individualsList[posOfWorstGuy] = child

    def getIndividualsList(self):
        return self.__individualsList
