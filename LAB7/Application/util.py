from math import sqrt


def normaliseData(noExamples, noFeatures, trainData, noTestExamples, testData):
    # statistical normalisation
    for j in range(noFeatures):
        summ = 0.0
        for i in range(noExamples):
            summ += trainData[i][j]
        mean = summ / noExamples
        squareSum = 0.0
        for i in range(noExamples):
            squareSum += (trainData[i][j] - mean) ** 2
        deviation = sqrt(squareSum / noExamples)
        for i in range(noExamples):
            trainData[i][j] = (trainData[i][j] - mean) / deviation
        for i in range(noTestExamples):
            testData[i][j] = (testData[i][j] - mean) / deviation
            # min-max normalization


def readData(fileName):
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


def normaliseData2(noExamples, noFeatures, trainData, noTestExamples, testData):
    for j in range(noFeatures):
        minn = min([trainData[i][j] for i in range(noExamples)])
        maxx = max([trainData[i][j] for i in range(noExamples)])
        for i in range(noExamples):
            trainData[i][j] = (trainData[i][j]-minn)/(maxx-minn)
        for i in range(noTestExamples):
            testData[i][j] = (trainData[i][j]-minn)/(maxx-minn)
