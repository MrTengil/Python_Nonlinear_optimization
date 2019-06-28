from numpy import *
from nonlinmin import *
import matplotlib.pyplot as plt


# Anonoumus function
def f(x):
    return x[0]**2 + x[1]**2
x1 = array([2, 3])
tol = 10**(-6)

[x, counter, xs] = nonlinmin(f, x1, tol)   # Default value of tolerance (tol) set to 10**(-6) if not specified

print('x1:', x1)
print('tol:', tol)
print('Function value at starting guess:', f(x1))

print('Startguess: ', x1)
print('Converged point: ', x)
print('Number of iterations:', counter)
xs = xs.flatten()
print('STeps taken:', xs)
