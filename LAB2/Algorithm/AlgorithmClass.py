from math import sqrt

from Population.PopulationClass import Population
from Problem.Problem import Problem

import matplotlib.pyplot as plt


class Algorithm:
    def __init__(self):
        self.__problem = None
        self.__population = None
        self.__iterationsDone = 0
        self.__maxNumberIterations = None
        self.__mutationProbability = None

    def readParameters(self, fileName):
        f = open(fileName, "r")
        problemDataFileName = f.readline().strip()
        popSize = int(f.readline().strip())
        nrIterations = int(f.readline().strip())
        mutationProbability = float(f.readline().strip())

        self.__problem = Problem(problemDataFileName)
        self.__population = Population(popSize, self.__problem.getCollectionSize())
        self.__maxNumberIterations = nrIterations
        self.__mutationProbability = mutationProbability

    def iteration(self):
        parent1, parent2 = self.__population.selectParents()
        child = parent1.crossover(parent2)
        child.mutate(self.__mutationProbability)
        self.__population.selectSurvivor(child, self.__problem)

    def printBestIndividual(self):
        evaluation = self.__population.evaluate(self.__problem)
        evaluation = sorted(evaluation, key=lambda x: x[1])
        bestIndividualPos = evaluation[-1][0]
        bestIndividual = self.__population.getIndividualsList()[bestIndividualPos]
        totalWeight = 0
        for i in range(0, bestIndividual.getIndividualSize()):
            if bestIndividual.getObjectsTaken()[i] == 1:
                item = self.__problem.getJewelryCollection()[i]
                totalWeight += item[1]
                print(item)
        print("Total cost " + str(bestIndividual.fitness(self.__problem)))
        print("Total weight: " + str(totalWeight))

    def run(self):
        self.readParameters("algorithmData")
        while self.__iterationsDone < self.__maxNumberIterations:
            self.iteration()
            self.__iterationsDone += 1
        self.printBestIndividual()

    def statistics(self):
        bestValuesObtained = []
        for i in range(30):
            bestFitness = Algorithm().__doOneStatisticRun()
            bestValuesObtained.append(bestFitness)
        # now we will compute the standard deviation and the mean
        s = sum(bestValuesObtained, 0)
        mean = s / len(bestValuesObtained)

        recompArray = []
        for val in bestValuesObtained:
            recompArray.append((val - mean) * (val - mean))
        s2 = sum(recompArray, 0)
        m2 = s2 / len(recompArray)
        standardDeviation = sqrt(m2)

        print("Statistics result: ")
        print(" Mean: " + str(mean))
        print(" Standard Deviation: " + str(standardDeviation))

        return Algorithm().__doOnePlot()

    def __doOneStatisticRun(self):
        self.readParameters("statisticsAlgorithmData")
        while self.__iterationsDone < self.__maxNumberIterations:
            self.iteration()
            self.__iterationsDone += 1
        evaluation = self.__population.evaluate(self.__problem)
        evaluation = sorted(evaluation, key=lambda x: x[1])
        return evaluation[-1][1]

    def __doOnePlot(self):
        self.readParameters("statisticsAlgorithmData")
        values = []
        while self.__iterationsDone < self.__maxNumberIterations:
            self.iteration()
            self.__iterationsDone += 1
            evaluation = self.__population.evaluate(self.__problem)
            mean = sum(j for i, j in evaluation) / len(evaluation)
            values.append(mean)
        iterations = [i for i in range(1, 1001)]
        plt.plot(iterations, values)
        plt.xlabel("Iterations")
        plt.ylabel("Fitness")
        return plt
        # plt.show()