from math import sqrt


class Problem:
    def __init__(self, file_name):
        self.__noTrainExamples = None
        self.__noFeatures = None
        self.__noOutputs = None
        self.__inTrainData = None
        self.__outTrainData = None
        self.__noTrainExamples, self.__noFeatures, self.__noOutputs, self.__inTrainData, self.__outTrainData = self.readData(file_name)
        self.normaliseData2(self.__noTrainExamples, self.__noFeatures, self.__inTrainData, 1, self.__outTrainData )
       # print(self.__inTrainData)
       # print(self.__outTrainData)

    def getNoTrainExamples(self):
        return self.__noTrainExamples

    def getNoFeatures(self):
        return self.__noFeatures

    def getNoOutputs(self):
        return self.__noOutputs

    def getInTrainData(self):
        return self.__inTrainData

    def getOutTrainData(self):
        return self.__outTrainData

    def normaliseData2(self, noExamples, noFeatures, trainData, noOutputFeatures, trainOutputData):
        for j in range(noFeatures):
            minn = min([trainData[i][j] for i in range(noExamples)])
            maxx = max([trainData[i][j] for i in range(noExamples)])
            for i in range(noExamples):
                trainData[i][j] = (trainData[i][j] - minn) / (maxx - minn)
            #for i in range(noTestExamples):
             #   testData[i][j] = (trainData[i][j] - minn) / (maxx - minn)
        for j in range(noOutputFeatures):
            minn = min([trainOutputData[i][j] for i in range(noExamples)])
            maxx = max([trainOutputData[i][j] for i in range(noExamples)])
            for i in range(noExamples):
                trainOutputData[i][j] = (trainOutputData[i][j] - minn) / (maxx - minn)


    def readData(self, fileName):
        f = open(fileName, "r")
        noTrainExamples = int(f.readline().strip())
        noFeatures = int(f.readline().strip())
        noOutputs = int(f.readline().strip())
        inTrainData = []
        outTrainData = []
        for i in range(noTrainExamples):
            line = f.readline().strip()
            attrs = line.split(",")
            oneInput = []
            jj = 0
            for j in range(noFeatures):
                oneInput.append(float(attrs[j]))
                jj = j
            oneOutput = []
            for j in range(noOutputs):
                oneOutput.append(float(attrs[jj + j + 1]))
            inTrainData.append(oneInput)
            outTrainData.append(oneOutput)
        f.close()
        return noTrainExamples, noFeatures, noOutputs, inTrainData, outTrainData

