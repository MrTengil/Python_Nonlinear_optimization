from Hessian import *
from Gradient import *
from distance import *
import numpy as np

def nonlinmin(f, x1, tol = 10**(-6)):
    # x1 is the point at which we would like to find the Hessian

    # Make sure that the guess is a row-vector
    # WRONG! INSTEAD MAKE SURE ITS A COLUMN VECTOR
    #cd = x1.shape
    #if (len(cd) == 1):
    #    x1 = np.array(x1)[np.newaxis]
    #    x1 = x1.T
    #print('len(cd) =', len(cd))

    ab = x1.size  # What is the dimension of the problem
    print('x1')
    print(x1)
    H = Hessian(f, x1, ab)
    G = Gradient(f, x1, ab)
    x = np.zeros(ab)
    HG = np.linalg.solve(H, G)
    x2 = x1 - HG.T
    x = x1
    count = 1
    x2 = x2.flatten()       # Previous steps creates arrays within arrays. This fixes this. Still new. Let me be!
    x = x.flatten()         # Previous steps creates arrays within arrays. This fixes this. Still new. Let me be!
    d = distance(x2, x, ab)
    while (d > tol):
        x2 = x
        H = Hessian(f, x, ab)
        G = Gradient(f, x, ab)
        HG = np.linalg.solve(H, G)
        x = x2 - HG.T
        x2 = x2.flatten()   # Previous steps creates arrays within arrays. This fixes this. Still new. Let me be!
        x = x.flatten()     # Previous steps creates arrays within arrays. This fixes this. Still new. Let me be!
        d = distance(x2, x, ab)
        count = count + 1
    xs = np.array([1, 2, 3], float)
    return(x, count, xs)