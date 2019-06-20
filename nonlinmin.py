from Hessian import *
from Gradient import *
import numpy as np

def nonlinmin(f, x1, tol = 10**(-6)):
    # x1 is the point at which we would like to find the Hessian
    ab = x1.size  # What is the dimension of the problem
    H = Hessian(f, x1, ab)
    G = Gradient(f, x1, ab)
    x = np.zeros(ab)
    x2 = x1 - np.linalg.solve(H,G)
    x = x1
    count = 1
    while (np.absolute(x2 - x)> tol):
        x2 = x
        H = Hessian(f, x, ab)
        G = Gradient(f, x, ab)
        x = x2 - np.linalg.solve(H,G)
        count = count + 1

    return(x, count)