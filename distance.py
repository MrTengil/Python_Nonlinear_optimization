import numpy as np

def distance(x1, x2, ab):
    a = np.empty(ab)
    for i in range(ab):
        print('x1[i]', x1[i])
        print('x2[i]', x2[i])
        a[i] = (x2[i] - x1[i])**2
    asum = sum(a)
    d = np.sqrt(asum)
    return d