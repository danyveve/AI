import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# the activation function:
from util import normaliseData, readData, normaliseData2


def sigmoid(x):
    return 1.0 / (1 + np.exp(-x))


# the derivate of te activation function
def sigmoid_derivative(x):
    return x * (1.0 - x)


def Leaky(x):
    if (x > 0):
        return x
    else:
        return 0.01 * x


def dLeaky(x):
    if (x > 0):
        return 1
    else:
        return 0.01


def LeakyArray(a):
    result = []
    for i in range(a.shape[0]):
        part = []
        for j in range(a.shape[1]):
            part.append(Leaky(a[i][j]))
        result.append(part)
    return np.array(result)


def dLeakyArray(a):
    result = []
    for i in range(a.shape[0]):
        part = []
        for j in range(a.shape[1]):
            part.append(dLeaky(a[i][j]))
        result.append(part)
    return np.array(result)


class NeuralNetwork:
    # constructor for this VERY particular network with 2 layers (plus one for input)

    def __init__(self, x, y):
        self.input = x
        self.weights1 = np.random.rand(self.input.shape[1], 25)
        self.y = y
        self.weights2 = np.random.rand(25, 1)
        self.output = np.zeros(self.y.shape)
        self.loss = []
        self.learning = 0.25

    # the function that computs the output of the network for some input
    def feedforward(self):
        self.layer1 = sigmoid(np.dot(self.input, self.weights1))
        self.output = sigmoid(np.dot(self.layer1, self.weights2))

    # the backpropagation algorithm
    def backprop(self):
        # application of the chain rule to find derivative of the
        # loss function with respect to weights2 and weights1
        # print(self.output)
        d_weights2 = np.dot(self.layer1.T, (2 * (self.y - self.output) *
                                            sigmoid_derivative(self.output)))

        d_weights1 = np.dot(self.input.T, (np.dot(2 * (self.y -
                                                       self.output) * sigmoid_derivative(self.output),
                                                  self.weights2.T) *
                                           sigmoid_derivative(self.layer1)))
        # update the weights with the derivative (slope) of the loss function
        # print(d_weights1.shape)
        self.weights1 += d_weights1 * self.learning
        self.weights2 += d_weights2 * self.learning
        # print(sum((self.y - self.output) ** 2))
        # print(((self.y-self.output)**2))

        # print(sum(sum((self.y - self.output) ** 2)) / 4)
        # print(self.y)
        # print("####")
        # print(self.output)
        # print("%%%")
        # print(self.y, self.output)
        self.loss.append(sum((self.y - self.output) ** 2))


if __name__ == "__main__":
    # X the array of inputs, y the array of outputs, 4 pairs in total

    noTrainExamples, noFeatures, noOutputs, inTrainData, outTrainData = readData("slump_test.data")
    noTestExamples, noFeatures, noOutputs, inTestData, outTestData = readData("slump_test.data")

    normaliseData(noTrainExamples, noFeatures, inTrainData, noTestExamples, inTestData)
    normaliseData2(noTrainExamples, 1, outTrainData, noTestExamples, outTestData)
    # for i in range(len(inTrainData)):
    # print(inTrainData[i])
    # print(outTrainData[i])
    inTrainData = np.array(inTrainData)
    outTrainData = np.array(outTrainData)

    nn = NeuralNetwork(inTrainData, outTrainData)

    nn.loss = []
    iterations = []
    for i in range(10000):
        nn.feedforward()
        nn.backprop()
        iterations.append(i)

    matches = 0
    for i in range(0, nn.y.shape[0]):
        if abs(nn.y[i][0] - nn.output[i][0]) < 0.05:
            matches += 1

    print(matches, "out of", noTrainExamples)

    plt.plot(iterations, nn.loss, label='loss value vs iteration')
    plt.xlabel('Iterations')
    plt.ylabel('loss function')
    plt.legend()
    plt.show()
