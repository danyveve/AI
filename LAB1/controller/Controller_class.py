import math
import queue


class Controller:
    def __init__(self, problem):
        self.__problem = problem

    def getProblem(self):
        return self.__problem

    def BFS(self, root):

        q = [root]

        while len(q) > 0:
            currentState = q.pop(0)
            #print(str(currentState))
            if not self.cutEdge(currentState.getValues()):
                if self.isSolution(currentState.getValues()):
                    return self.constructBoardWithGivenConfig(currentState.getValues())
                q = q + self.__problem.expand(currentState)

    def BestFS(self, root):

        visited = []
        toVisit = [root]
        while len(toVisit) > 0:
            node = toVisit.pop(0)
            visited = visited + [node]
            if not self.cutEdge(node.getValues()):
               # print(str(node))
                if self.isSolution(node.getValues()):
                    return self.constructBoardWithGivenConfig(node.getValues())
                aux = []
                for x in self.__problem.expand(node):
                    if x not in visited:
                        aux.append(x)
                aux = [[x, self.__problem.heuristics(x)] for x in aux]
                aux.sort(key=lambda x: x[1])
                aux = [x[0] for x in aux]
                toVisit = aux[:] + toVisit

    def BestFS2(self, root):
        visited = []
        toVisit = queue.PriorityQueue()
        toVisit.put((self.__problem.heuristics(root), root))

        while toVisit.qsize() > 0:
            node = toVisit.get()[1]
            visited = visited + [node]
            if not self.cutEdge(node.getValues()):
                #print(str(node))
                if self.isSolution(node.getValues()):
                    return self.constructBoardWithGivenConfig(node.getValues())
                for x in self.__problem.expand(node):
                    if x not in visited:
                        toVisit.put((self.__problem.heuristics(x), x))

    def isSolution(self, configVector):
        # if there are zeros on configVector, return False
        if 0 in configVector:
            return False

        #if there is a digit which didn`t appear as many times as it should, return False
        boardSize = self.__problem.getSudokuSize()
        recomputedFreqVector = self.__problem.getFrequencyVector()[:]
        for el in configVector:
            recomputedFreqVector[el - 1] += 1
        for el in recomputedFreqVector:
            if el != boardSize:
                return False

        # construct board
        completedBoard = self.constructBoardWithGivenConfig(configVector)


        #check constraints:
        #1.uniqueness on line
        for i in range(boardSize):
            if len(completedBoard[i]) > len(set(completedBoard[i])):
                return False
        #2.uniqueness on column
        for j in range(boardSize):
            column = []
            for i in range(boardSize):
                column.append(completedBoard[i][j])
            if len(column) > len(set(column)):
                return False

        #3.uniqueness on squared boxes
        squaredFactor = int(math.sqrt(boardSize))
        for row in range (0, boardSize, squaredFactor):
            for col in range(0, boardSize, squaredFactor):
                square = []
                for i in range(0,squaredFactor):
                    for j in range(0,squaredFactor):
                        square.append(completedBoard[row+i][col+j])
                if len(square) > len(set(square)):
                    return False

        return True

    def constructBoardWithGivenConfig(self, configVector):
        currentGap = 0
        originalInitBoard = self.__problem.getInitialBoard()
        completedBoard = []
        for i in range(len(originalInitBoard)):
            completedBoard.append(originalInitBoard[i][:])
        for i in range(self.__problem.getSudokuSize()):
            for j in range(self.__problem.getSudokuSize()):
                if (completedBoard[i][j] == 0):
                    completedBoard[i][j] = configVector[currentGap]
                    currentGap += 1

        return completedBoard

    def cutEdge(self, configVector):
        completedBoard = self.constructBoardWithGivenConfig(configVector)
        boardSize = self.__problem.getSudokuSize()

        # 1.uniqueness on line
        for i in range(boardSize):
            filteredLine = list(filter((0).__ne__, completedBoard[i]))
            if len(filteredLine) > len(set(filteredLine)): #means we have dups on line
                return True

        # 2.uniqueness on column
        for j in range(boardSize):
            column = []
            for i in range(boardSize):
                column.append(completedBoard[i][j])
            filteredColumn = list(filter((0).__ne__, column))
            if len(filteredColumn) > len(set(filteredColumn)):
                return True

        # 3.uniqueness on squared boxes
        squaredFactor = int(math.sqrt(boardSize))
        for row in range(0, boardSize, squaredFactor):
            for col in range(0, boardSize, squaredFactor):
                square = []
                for i in range(0, squaredFactor):
                    for j in range(0, squaredFactor):
                        square.append(completedBoard[row + i][col + j])
                filteredSquare = list(filter((0).__ne__, square))
                if len(filteredSquare) > len(set(filteredSquare)):
                    return True

        # 4.numbers of appearances exceeded
        recomputedFreqVector = self.__problem.getFrequencyVector()[:]
        filteredConfigVector = list(filter((0).__ne__, configVector))
        for el in filteredConfigVector:
            recomputedFreqVector[el - 1] += 1
        for el in recomputedFreqVector:
            if el > boardSize:
                return True

        return False

