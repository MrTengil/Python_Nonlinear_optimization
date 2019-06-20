import numpy as np

def Gradient(f, x, ab):
    h = np.finfo(float).eps**0.5 # Alter the small step h from machine epsilon
    e = np.eye(ab, ab)           #
    G = np.zeros((ab, ab),float) # Initiate the Hessian matrix
    for i in range(ab):
        G[i] = (f(x + h*e[:,i]) - f(x))/h
    return G