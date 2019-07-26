import numpy as np


def sigmoid(x):
    return 1 / (1 + (np.exp(-x)))


def sigmoid_derivative(x):
    a = sigmoid(x)
    return a * (1 - a)
