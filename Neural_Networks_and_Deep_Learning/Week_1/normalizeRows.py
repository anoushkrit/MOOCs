import numpy as np


def normalizeRows(x):
    """ A function to implement and normalize each row of the matrix or numpy array x (to have unit length)
    Division of x with its normalized values"""
    x_norm = np.linalg.norm(x, axis=1, keepdims=True)
    return x/x_norm
