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
        self.__population = Population(popSize)
        self.__maxNumberIterations = nrIterations
        self.__mutationProbability = mutationProbability

    def iteration(self):
        parent1, parent2 = self.__population.selectParents()
        child = parent1.crossover(parent2)
        child.mutate(self.__mutationProbability)
        self.__population.selectSurvivor(child, self.__problem)


    def run(self):
        self.readParameters("algorithmData")
        evaluation = []
        while self.__iterationsDone < self.__maxNumberIterations:
            self.iteration()
            self.__iterationsDone += 1
            curr_eval = self.__population.evaluate(self.__problem)
            curr_eval = sorted(evaluation, key=lambda x: x[1])
            evaluation.append(curr_eval[-1][1])
            #self.printBestIndividual()

    def statistics(self):
        bestValuesObtained = []
        for i in range(1):
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

        return Algorithm().doOnePlot()

    def __doOneStatisticRun(self):
        self.readParameters("statisticsAlgorithmData")
        while self.__iterationsDone < self.__maxNumberIterations:
            self.iteration()
            self.__iterationsDone += 1
        evaluation = self.__population.evaluate(self.__problem)
        evaluation = sorted(evaluation, key=lambda x: x[1])
        return evaluation[-1][1]

    def doOnePlot(self):
        self.readParameters("statisticsAlgorithmData")
        values = []
        found = False
        while self.__iterationsDone < self.__maxNumberIterations or not found:
           # print(self.__iterationsDone)
            self.iteration()
            self.__iterationsDone += 1
            evaluation = self.__population.evaluate(self.__problem)
            mean = sum(j for i, j in evaluation) / len(evaluation)
            values.append(mean)
            evaluation = sorted(evaluation, key=lambda x: x[1])
            if evaluation[0][1] < 0.5:
                found = True
        iterations = [i for i in range(1, len(values) + 1)]
        plt.plot(iterations, values)
        plt.xlabel("Iterations")
        plt.ylabel("Fitness")
        return plt
        # plt.show()