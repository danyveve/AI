from state.State_class import State
import traceback

class Problem:
    def __init__(self, fileName):
        self.__gaps = 0
        self.__sudokuSize = 0
        self.__initialState = []
        self.__frequencyVector = []
        self.__initialBoard = []
        self.readFromFile(fileName)

    def getRoot(self):
        return self.__initialState

    def getFrequencyVector(self):
        return self.__frequencyVector

    def getInitialBoard(self):
        return self.__initialBoard

    def getGaps(self):
        return self.__gaps

    def getSudokuSize(self):
        return self.__sudokuSize

    def expand(self, currentState):
        myList = []
        #for j in range(currentState.getSize()):
        j = 0
        while j < currentState.getSize() and currentState.getValues()[j] != 0:
            j += 1
        if j < currentState.getSize():
            for x in currentState.nextStates(j):
                myList.append(x)

        return myList

#       (0,0,0,0,0,0,0)
        (1,0,0,0,0,0)
        state = (1, 7, 0,0,0,0,)


    def heuristics(self, state):
        #recompute the frequency vector
        last_value_added = 0
        newFreqVector = self.__frequencyVector[:]
        for i in range(self.__gaps):
            cv = state.getValues()[i]
            if(cv != 0):
                last_value_added = cv
                newFreqVector[cv-1] = newFreqVector[cv-1] + 1

        return newFreqVector[last_value_added-1]

    def readFromFile(self, fileName):
        try:
            f = open(fileName, "r")
            #get sudoku size
            line = f.readline().strip()
            self.__sudokuSize = int(line)
            #initialize frequency vector
            self.__frequencyVector = [0 for i in range(self.__sudokuSize)]

            #build initial board
            for i in range(self.__sudokuSize):
                newRow = []
                line = f.readline().strip()
                attrs = line.split(" ")
                for j in range (self.__sudokuSize):
                    cellValue = int(attrs[j])
                    if(cellValue == 0):
                        self.__gaps = self.__gaps + 1
                    else:
                        self.__frequencyVector[cellValue-1]+=1
                    newRow.append(cellValue)
                self.__initialBoard.append(newRow)

            #build initial state Vector
            initVect = [0 for i in range(self.__gaps)]
            self.__initialState = State(initVect, self.__sudokuSize)
        except Exception:
            traceback.print_exc()
        finally:
            f.close()