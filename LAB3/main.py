from Controller.ControllerClass import Controller


def main():
    Controller("parameters1.in", "problem1.in").runAlg()
    Controller.runStatistics()
main()