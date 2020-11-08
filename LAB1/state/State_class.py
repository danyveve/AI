class State:
    '''
        Holds the state(configuration) of the board
        '''

    def __init__(self, values_to_complete, sudoku_size):
        self.__size = len(values_to_complete)
        self.__values = values_to_complete[:]
        self.__sudoku_size = sudoku_size

    def getSize(self):
        return self.__size

    def setSize(self, size):
        self.__size = size

    def getValues(self):
        return self.__values[:]

    def setValues(self, values):
        self.__values = values

    def getSudoku_size(self):
        return self.__sudoku_size

    def setSudoku_size(self, sudoku_size):
        self.__sudoku_size = sudoku_size

    def nextStates(self, j):
        '''
        Creates all the children of the current node state (fill on the position given position all the possible values from the sudoku range)
        in: the position of the last filled gap
        out: the list of the next correct configurations obtained moving this frog
        out: the list of the next configurations with the position j+1 filled with values from the sudoku range
        '''

        nextC = []

        if self.__values[j] == 0:
            for x in range(1, self.__sudoku_size + 1):
                aux = self.__values[:]
                aux[j] = x
                nextC.append(State(aux, self.__sudoku_size))

        return nextC

    def __eq__(self, other):
        if not isinstance(other, State):
            return False
        if self.__size != other.getSize() or self.__sudoku_size != other.getSudoku_size():
            return False
        for i in range(self.__size):
            if self.__values[i] != other.getValues()[i]:
                return False
        return True

    def __str__(self):
        return str(self.__values)

    def __lt__(self, other): #the one closer to finish
        countSelf = 0
        for i in self.__values:
            if i == 0:
                countSelf += 1

        countOther = 0
        for i in self.__values:
            if i == 0:
                countOther += 1

        #so it is true that self is smaller if it closer to finish
                return countSelf >= countOther
