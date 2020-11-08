from Algorithm.AlgorithmClass import Algorithm


class Application:
    def __init__(self):
        self.__algorithm = Algorithm()

    def main(self):
        plt = self.__algorithm.statistics()
        self.__algorithm.run()
        plt.show()


Application().main()
