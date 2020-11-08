from random import randint, random
'''
Some specific functions for a GP variation
'''

from random import randint,random

DEPTH_MAX=5
terminals=['C','S','F','W','SP','COA','FIA']
noTerminals=7
functions=['+','-','*']
noFunctions=3

class Individual:
    def __init__(self, d=DEPTH_MAX):
        self.mDepth=d
        self.repres=[0 for i in range(2**(self.mDepth+1)-1)]
        self.fitness=0
        self.size=0
        self.growExpression()

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
            err += crtOut[d][0]-self.evalExpression(0, crtData[d])[0]
        self.fitness = err
        return abs(self.fitness)

    def traverse(self,pos):
        '''
        returns the next index where it begins the next
        branch in the tree from the same level
        '''
        if (self.repres[pos] > 0):	 #terminal
            return pos+1
        else:
            return self.traverse(self.traverse(pos+1))

    def crossover(self, F):
        off=Individual()
        while True:
            startM = randint(0, self.size - 1)
            endM = self.traverse(startM)
            startF = randint(0,F.size-1)
            endF = F.traverse(startF)
            if (len(off.repres)>endM+(endF-startF-1)+(self.size-endM-1)):
                break
        i=-1
        for i in range(startM):
            off.repres[i] = self.repres[i]
        for j in range(startF, endF):
            i=i+1
            off.repres[i] = F.repres[j]
        for j in range(endM, self.size):
            i=i+1
            off.repres[i] = self.repres[j]
        off.size=i+1
        return off

    def mutate(self, probability):
        if probability > random():
            off=Individual()
            pos = randint(0, self.size)
            off.repres = self.repres[:]
            off.size=self.size
            if off.repres[pos] > 0:	#terminal
                off.repres[pos] = randint(1,noTerminals)
            else:	#function
                off.repres[pos] = -randint(1,noFunctions)
            self.repres = off.repres[:]