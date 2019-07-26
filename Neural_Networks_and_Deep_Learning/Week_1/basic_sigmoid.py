import math
import numpy as np

""" The formula for sigmoid is S(x) = 1/(1+exp(-x))"""


def basic_sigmoid(x):
    return 1/(1+math.exp(-x))


def sigmoid(x):
    return 1/(1+(np.exp(-x)))


def sigmoid_derivative(x):
    a = sigmoid(x)
    return a*(1-a)

