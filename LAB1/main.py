from controller.Controller_class import Controller
from problem.Problem_class import Problem
from tests.testing import tests
from ui.Ui_class import UI


def main():
    tests()
    fileName = input("give input file >>")
    problem = Problem(fileName)
    controler = Controller(problem)
    ui = UI(controler)
    ui.run()

main()
