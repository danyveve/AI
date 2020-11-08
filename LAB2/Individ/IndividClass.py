from random import randint, random


class Individual:
    '''
    Individual is (x1,...,xn)
    where xi = | 1, if object i is IN
               | 0, if object i is OUT
    '''

    def __init__(self, size):
        self.__individualSize = size
        self.__objectsTaken = [randint(0, 1) for i in range(size)]

    def getIndividualSize(self):
        return self.__individualSize

    def getObjectsTaken(self):
        return self.__objectsTaken

    def __setObjectsTaken(self, l):
        self.__objectsTaken = l

    def fitness(self, problem):
        jewelryCollection = problem.getJewelryCollection()
        maximumWeight = problem.getMaximumWeight()
        sumValue = 0
        sumWeight = 0
        totalWeight = 0
        for i in range(self.__individualSize):
            sumValue = sumValue + jewelryCollection[i][0] * self.__objectsTaken[i]
            sumWeight = sumWeight + jewelryCollection[i][1] * self.__objectsTaken[i]
            totalWeight = totalWeight + jewelryCollection[i][1]
        if sumWeight <= maximumWeight:
            return sumValue
        else:
            # penalty with a percentage of the maximum weight
            overflowPercentage = (sumWeight - maximumWeight) * 100 / maximumWeight
            penalty = sumValue / 100 * (100 - overflowPercentage)
            return (100 - overflowPercentage) / 100 * (sumValue - penalty)

    def mutate(self, probability):
        if probability > random():
            position = randint(0, self.__individualSize - 1)
            # self.__objectsTaken[position] = randint(0, 1)
            self.__objectsTaken[position] = (self.__objectsTaken[position] + 1) % 2

    def crossover(self, parent2):
        child = Individual(self.__individualSize)
        childObjectsTaken = []
        for i in range(self.__individualSize):
            if random() <= 0.5:
                childObjectsTaken.append(self.__objectsTaken[i])
            else:
                childObjectsTaken.append(parent2.getObjectsTaken()[i])
        child.__setObjectsTaken(childObjectsTaken)
        return child

'''
Some specific functions for a GP variation
'''

from random import randint,random

DEPTH_MAX=5
terminals=['U','RS','V','c1','c2','c3','c4','c5']
noTerminals=8
functions=['+','-','*']
noFunctions=3

class Chromosome:
    def __init__(self, d=DEPTH_MAX):
        self.mDepth=d
        self.repres=[0 for i in range(2**(self.mDepth+1)-1)]
        self.fitness=0
        self.size=0

    def growExpression(self, pos=0, depth=0):
        """
        initialise randomly an expression
        """
        if (pos==0)or(depth<self.mDepth):
            if random()<0.5:
                self.repres[pos] = randint(1, noTerminals)
                self.size=pos+1
                return pos + 1
            else:
                self.repres[pos] = -randint(1,noFunctions)
                finalFirstChild =self.growExpression(pos+1, depth+1)
                finalSecondChild = self.growExpression(finalFirstChild, depth+1)
                return finalSecondChild
        else:
                #choose a terminal
            self.repres[pos] = randint(1, noTerminals)
            self.size=pos+1
            return pos + 1

    def evalExpression(self, pos, crtData):
        """
        the expresion value for some specific terminals
        """
        if  self.repres[pos]>0: # a terminal
            return crtData[self.repres[pos]-1], pos
        elif self.repres[pos]<0:  #a function
            if functions[-self.repres[pos]-1]=='+':
                auxFirst=self.evalExpression(pos+1,crtData)
                auxSecond=self.evalExpression(auxFirst[1]+1,crtData)
                return auxFirst[0]+auxSecond[0],auxSecond[1]
            elif functions[-1-self.repres[pos]]=='-':
                auxFirst=self.evalExpression(pos+1,crtData)
                auxSecond=self.evalExpression(auxFirst[1]+1,crtData)
                return auxFirst[0]-auxSecond[0],auxSecond[1]
            elif functions[-1-self.repres[pos]]=='*':
                auxFirst=self.evalExpression(pos+1,crtData)
                auxSecond=self.evalExpression(auxFirst[1]+1,crtData)
                return auxFirst[0]*auxSecond[0],auxSecond[1]

    def computeFitness(self, crtData,crtOut,noExamples):
        '''
        the fitness function
        '''
        err = 0.0
        for d in range(noExamples):
            err += crtOut[d]-self.evalExpression(0, crtData[d])
        self.fitness = err

    def traverse(self,pos):
        '''
        returns the next index where it begins the next
        branch in the tree from the same level
        '''
        if (self.repres[pos] > 0):	 #terminal
            return pos+1
        else:
            return self.traverse(self.traverse(pos+1))

    def crossover(M,F):
        off=Chromosome()
        while True:
            startM = randint(0,M.size-1)
            endM = M.traverse(startM)
            startF = randint(0,F.size-1)
            endF = F.traverse(startF)
            if (len(off.repres)>endM+(endF-startF-1)+(M.size-endM-1)):
                break
        i=-1
        for i in range(startM):
            off.repres[i] = M.repres[i]
        for j in range(startF, endF):
            i=i+1
            off.repres[i] = F.repres[j]
        for j in range(endM,M.size):
            i=i+1
            off.repres[i] = M.repres[j]
        off.size=i+1
        return off

    def mutation(c):
        off=Chromosome()
        pos = randint(0,c.size)
        off.repres = c.repres[:]
        off.size=c.size
        if off.repres[pos] > 0:	#terminal
            off.repres[pos] = randint(1,noTerminals)
        else:	#function
            off.repres[pos] = -randint(1,noFunctions)
        return off