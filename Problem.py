from numpy import *
from nonlinmin import *
import matplotlib.pyplot as plt


# Anonoumus function
def f(x):
    return x[0]**2 + x[1]**2
x1 = array([2, 3])
tol = 10**(-6)
print('x1:', x1, 'tol', tol)
print('funktion:', f(x1))
x = nonlinmin(f, x1, tol)   # Default value of tolerance (tol) set to 10**(-6) if not specified

print('Startgissning: ', x1)
print('Slutpunkt: ', x[0])
print('Tog så här många iteration:', x[1])
print('Stegen tagna:', x[2])