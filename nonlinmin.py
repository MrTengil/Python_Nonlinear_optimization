from Hessian import *
from Gradient import *
from distance import *
import numpy as np

def nonlinmin(f, x1, tol = 10**(-6), maxit = 16):
    ab = x1.size            # The dimension of the problem
    # x1 is the point at which we would like to find the Hessian
    xs = np.empty(([ab, 1]))    # Initiate the 2d array to save steps
    # Make sure that the guess is a row-vector
    # WRONG! INSTEAD MAKE SURE ITS A COLUMN VECTOR
    #cd = x1.shape
    #if (len(cd) == 1):
    #    x1 = np.array(x1)[np.newaxis]
    #    x1 = x1.T
    #print('len(cd) =', len(cd))

    H = Hessian(f, x1, ab)
    G = Gradient(f, x1, ab)
    HG = np.linalg.solve(H, G)  # G^(-1)*H
    x2 = x1 - HG.T              # Newton step
    x = x1
    xs = x
    count = 1               # Initiate counter
    x2 = x2.flatten()       # Previous steps creates arrays within arrays. This fixes this. Still new. Let me be!
    x = x.flatten()         # Previous steps creates arrays within arrays. This fixes this. Still new. Let me be!
    d = distance(x2, x, ab)     # How far have we traveled?
    while (d > tol) and (count < maxit):            # If traveled further than the tolerance, continue
        x2 = x
        H = Hessian(f, x, ab)
        G = Gradient(f, x, ab)
        HG = np.linalg.solve(H, G)
        x = x2 - HG.T
        x2 = x2.flatten()           # Previous steps creates arrays within arrays. This fixes this. Still new. Let me be!
        x = x.flatten()             # Previous steps creates arrays within arrays. This fixes this. Still new. Let me be!
        d = distance(x2, x, ab)     # Distance traveled
        xs = np.vstack((xs, x))     # Save the steps
        count = count + 1           # Increment the counter
    xs = xs.T   # Transposes the steps
    return(x, count, xs)