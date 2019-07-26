import numpy as np


def softmax(x):
    """Calculates the softmax for x(numpy array, matrix, vector, of any shape)"""
    return np.exp(x) / np.sum(np.exp(x),  axis=1, keepdims=True)

