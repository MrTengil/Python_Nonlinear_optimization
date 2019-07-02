'''
    Written by: Oskar Tengberg, 2019
                https://github.com/MrTengil

    This function generates the gradient of a function "f" at position "x" using the forward difference method.
    [Input]
        f = function
        x = point (1D-array)
        ab = dimension of the problem (integer)
    [Output]
        G = gradient (1D-array)

'''

import numpy as np

def Gradient(f, x, ab):
    h = np.finfo(float).eps**0.5    # Alter the small step h from machine epsilon
    e = np.eye(ab, ab)
    G = np.zeros((ab, 1), float)    # Initiate the Gradient vector
    for i in range(ab):
        G[i] = (f(x + h*e[:, i]) - f(x))/h  # Compute the gradient array
    return G