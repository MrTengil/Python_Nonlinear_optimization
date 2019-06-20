from numpy import *
import numpy as np

# x1 is the point at which we would like to find the Hessian
ab = x1.size  # What is the dimension of the problem

h = np.finfo(float).eps**0.33 # Alter the small step h from machine epsilon
e = eye(ab, ab)           #
H = zeros((ab, ab),float) # Initiate the Hessian matrix

for i in range(ab):
    for j in range(ab):
        H[i, j] = ( f(x1 + h*e[i] + h*e[j]) - f(x1 + h*e[i]) - f(x + h*e[j]) + f(x1))/(h*h)

