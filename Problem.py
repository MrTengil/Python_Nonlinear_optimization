'''
    Written by: Oskar Tengberg, 2019
                https://github.com/MrTengil

    This program is an example of how the "nonlinmin()" works. Post-processing is found further below for a
    2-dimensional problem.

    1. Define objective function
        - Input must be in array form (see below, "f(x)")
        - Objective function must be continuous, non-linear and must be twice derivable
    2. Define starting guess
        - Must be array form (see below, "x1")
    3. Call the minimization function from said starting guess
        - Objective function and starting guess is the only required input
        - Tolerance and maximum iteration is set by default if not assigned

'''

from numpy import *
from nonlinmin import *
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

# Objective function to minimize
def f(x):
    return x[0]**2 + x[1]**2
# Objective function for contour plot (ONLY FOR POST-PROCESSING OF TWO-DIMENSIONAL PROBLEM)
def fun(x, y):
    return x**2 + y**2
v_fun = vectorize(fun)  # Apparently this must be done for the post-processing

x1 = array([4, 3])      # Starting guess (must be a 1D array written as this)
tol = 10**(-8)          # Tolerance [Default is 10^^(-6)]
maxit = 32              # Maximum number of iterations [Default is 16]

[x, counter, xs] = nonlinmin(f, x1, tol, maxit)     # Call the minimization function!


print('Start guess: ', x1)
print('Function value at starting guess:', f(x1))


print('Converged point: ', x)
print('Function value at converged point:', f(x))
print('Number of iterations:', counter, '/', maxit)
print('Tolerance:', tol)
print('Steps taken:', xs)


# Post-processing, for a two-dimensional problem only!
ax = linspace(-5, 5, 400)
ay = linspace(-5, 5, 400)
xx, yy = meshgrid(ax, ay)
zz = v_fun(xx, yy)
# contour
plt.figure(1)
plt.contour(xx, yy, zz, 20)
plt.plot(xs[0][:], xs[1][:], '-o')

# 3D-plot
plt.figure(2)
ax = plt.axes(projection='3d')
ax.contour3D(xx, yy, zz, 50, cmap='binary')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()
