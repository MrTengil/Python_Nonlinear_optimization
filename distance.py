'''
    Written by: Oskar Tengberg, 2019
                https://github.com/MrTengil

    This function calculates the distance between two points.
    [Input]
        x1 = point 1 (1D-array)
        x2 = point 2 (1D-array)
        ab = dimension (integer)
    [Output]
        d = distance (float)

'''

import numpy as np

def distance(x1, x2, ab):
    a = np.empty(ab)
    for i in range(ab):
        a[i] = (x2[i] - x1[i])**2
    asum = sum(a)
    d = np.sqrt(asum)
    return d