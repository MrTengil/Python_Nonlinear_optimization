from numpy import *
import matplotlib.pyplot as plt

arr1 = array([1, 2, 3, 4, 5 , 6, 7, 8, 9, 10], float)

# Anonoumus function
def f(x):
    return x**2

arr2 = f(arr1)

mat = array([[1,2,3], [1, 2, 3]])
hej = mat.shape
print('Storlek på mat är')
print(mat.shape)

print('---')
print(mat)
print('---')
print(hej[1])

# print(arr1)
# plt.plot(arr1, arr2)
# plt.show()
# print('----')
# I = eye(3)
# print(I)