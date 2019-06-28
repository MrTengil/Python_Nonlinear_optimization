import numpy as np

def Hessian(f, x, ab):
    h = np.finfo(float).eps**0.33   # Alter the small step h from machine epsilon
    e = np.eye(ab, ab)
    H = np.zeros((ab, ab), float)   # Initiate the Hessian matrix
    for i in range(ab):
        for j in range(ab):
            H[i, j] = ( f(x + h*e[:, i] + h*e[:, j]) - f(x + h*e[:, i]) - f(x + h*e[:, j]) + f(x))/(h*h)
    return H
