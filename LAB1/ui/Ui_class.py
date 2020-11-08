import traceback
from time import time


class UI:
    def __init__(self, controler):
        self.__controler = controler

    def getControler(self):
        return self.__controler

    def printMenu(self):
        s = "\n"
        s += "1 - BFS \n"
        s += "2 - GBFS \n"
        s += "3 - GBFS2 \n"
        s += "0 - EXIT \n"
        s += "\n"
        print(s)

    def run(self):
        runM = True
        while runM:
            self.printMenu()
            try:
                command = int(input(">>"))
                if command == 0:
                    runM = False
                elif command == 1:
                    self.solveBFS()
                elif command == 2:
                    self.solveGBFS()
                elif command == 3:
                    self.solveGBFS2()
            except ValueError:
                print("Invalid command! \n")
            except Exception:
                traceback.print_exc()

    def solveBFS(self):
        startClock = time()
        solvedSudoku = self.__controler.BFS(self.__controler.getProblem().getRoot())
        for row in solvedSudoku:
            print(str(row))
        print('execution time = ', time() - startClock, " seconds")

    def solveGBFS(self):
        startClock = time()
        solvedSudoku = self.__controler.BestFS(self.__controler.getProblem().getRoot())
        print("====================================================")
        for row in solvedSudoku:
            print(str(row))
        print('execution time = ', time() - startClock, " seconds")

    def solveGBFS2(self):
        startClock = time()
        solvedSudoku = self.__controler.BestFS2(self.__controler.getProblem().getRoot())
        print("====================================================")
        for row in solvedSudoku:
            print(str(row))
        print('execution time = ', time() - startClock, " seconds")