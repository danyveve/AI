import traceback

from controller.ControllerClass import Controller


class View:
    def __init__(self):
        self.__controller = Controller()

    def printMenu(self):
        print("\n1.Introduce new texture and capacity in order to determine cycle type: ")
        print("2.Print the current cycle type")
        print("0.Exit\n")

    def run(self):
        runMenu = True
        while runMenu:
            self.printMenu()
            try:
                command = int(input(">>"))
                if command == 0:
                    runMenu = False
                elif command == 1:
                    self.determineCycleType()
                elif command == 2:
                    self.printCurrentCycleType()
            except ValueError:
                print("Invalid command! \n")
            except Exception:
                traceback.print_exc()

    def determineCycleType(self):
        try:
            texture = float(input("texture = "))
            capacity = float(input("capacity = "))
            self.__controller.determineCycleType(texture, capacity)
        except Exception:
            traceback.print_exc()

    def printCurrentCycleType(self):
        print(self.__controller.getCurrentCycleType())
