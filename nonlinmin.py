'''
    Written by: Oskar Tengberg, 2019
                https://github.com/MrTengil

    This function minimizes an n-dimensional function with the Newton method using the first and second derivative
    (gradient and hessian) of the function. The objective function must be continuous, non-linear and must be twice
    derivable.

    [Input]
        f = function
        x1 = starting guess (1D-array)
        tol = tolerance, default set to 10^(-6)
        maxit = maximum allowed iterations, default set to 16
    [Output]
        x = converged point
        count = number of iterations
        xs = steps taken

'''

from Hessian import *
from Gradient import *
from distance import *
import numpy as np

def nonlinmin(f, x1, tol = 10**(-6), maxit = 16):
    ab = x1.size                # The dimension of the problem
    xs = np.empty(([ab, 1]))    # Initiate the 2d array to save steps

    H = Hessian(f, x1, ab)
    G = Gradient(f, x1, ab)
    HG = np.linalg.solve(H, G)  # G^(-1)*H
    x2 = x1 - HG.T              # Newton step
    x = x1
    xs = x                      # Save the steps taken
    count = 1                   # Initiate counter
    x2 = x2.flatten()           # Previous steps creates arrays within arrays. This fixes this. Still new. Let me be!
    x = x.flatten()             # Previous steps creates arrays within arrays. This fixes this. Still new. Let me be!
    d = distance(x2, x, ab)     # How far have we traveled?
    while (d > tol) and (count < maxit):
        x2 = x
        H = Hessian(f, x, ab)
        G = Gradient(f, x, ab)
        HG = np.linalg.solve(H, G)  # G^(-1)*H
        x = x2 - HG.T               # Newton step
        x2 = x2.flatten()           # Previous steps creates arrays within arrays. This fixes this. Still new. Let me be!
        x = x.flatten()             # Previous steps creates arrays within arrays. This fixes this. Still new. Let me be!
        d = distance(x2, x, ab)     # Distance traveled
        xs = np.vstack((xs, x))     # Save the steps
        count = count + 1           # Increment the counter
    xs = xs.T   # Transposes the steps
    return x, count, xs
