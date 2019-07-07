'''
    Written by: Oskar Tengberg, 2019
                https://github.com/MrTengil

    This function generates the Hessian matrix of a function "f" at position "x" using the forward difference method.
    [Input]
        f = function
        x = point (1D-array)
        ab = dimension of the problem (integer)
    [Output]
        H = Hessian (2D-array)

'''

import numpy as np

def Hessian(f, x, ab):
    h = np.finfo(float).eps**0.33   # Alter the small step h from machine epsilon
    e = np.eye(ab, ab)
    H = np.zeros((ab, ab), float)   # Initiate the Hessian matrix
    for i in range(ab):
        for j in range(ab):
            H[i, j] = (f(x + h*e[:, i] + h*e[:, j]) - f(x + h*e[:, i]) - f(x + h*e[:, j]) + f(x))/(h*h)     # Compute the Hessian matrix
    return H
