from numpy import *
from nonlinmin import *
import matplotlib.pyplot as plt


# Objective function to minimize
def f(x):
    return x[0]**2 + x[1]**2

x1 = array([2, 3])  # Starting guess
tol = 10**(-6)      # Tolerance [Default is 10^^(-6)]
maxit = 10         # Maximum number of iterations [Default is 16]

[x, counter, xs] = nonlinmin(f, x1, tol, maxit)

xs = xs.flatten()   # Fix the steps taken

print('Startguess: ', x1)
print('Function value at starting guess:', f(x1))
print('Tolerance:', tol)

print('Converged point: ', x)
print('Function value at converged point:', f(x))
print('Number of iterations:', counter, '/', maxit)


print('STeps taken:', xs)
