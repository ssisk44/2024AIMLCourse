import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# a1 = np.array([1,2,3,4,5])
# print("a1, type(a1): ", a1, type(a1))
# print(a1.shape())
# a2 = np.array([1,2,3,4,5])
# print(a2 , type(a2))
# print(a1+a2)
# print(a1-a2)
# print(a1*a2)
# print(a1.dtype)
# print(np.square(a1))
# print(np.sqrt(a1))
#
# a3 = np.array([1.011, 2.023, 4.0201])
# print("a3: ", a3)
# print("a3 rounded to two decimals: ", np.round(a3, 2))
# print("a3 floor: ", np.floor(a3))
# print("a3 ceil: ", np.ceil(a3))
#
# a4 = np.array([3, -5, 7, -9])
# print("Array a4: ", a4)
# print("Absolute value of a4: ", np.abs(a4))
# print("a4 to the power of 3: ", np.power(a4, 3))
# print("a4 ndim: ", a4.ndim)

# a5 = [[1,3], [2,4]]
# a6 = [[10, 30], [20, 40]]
# print("a5: ", a5)
# print("a6: ", a6)
# res = np.dot(a5, a6)
# #res = np.matmul(a5, a6)
# print("a5 a6 matrix multiply: ", np.dot(a5, a6))
# print("arange (exclusive max): ", np.arange(0,5,1))
# print("arange (exclusive max only): ", np.arange(5))
# print(np.arange(5, 51, 5))
# print(np.arange(50, 4, -5))

a7 = np.array([5,10,15,20,25,30,35,40,45,50])
# # print("a7: ", a7)
# # print(a7*10)
# print(a7.min(), a7.max(), a7.mean(), a7.std())
# print(a7.argmin(), a7.argmax())
# print(26 > a7)  # return boolean value array for statement
# print(a7[a7 > 25])  # get all values greater than
print(a7[(a7>13) | (a7<24)])

# a8 = np.array([
#     [1, 2, 3, 4],
#     [10, 20, 30, 40],
#     [100, 200, 300, 400]
# ])
# 2D np.array indexing
# print(a8[1:2, 1:])
# print(a8[1:, :-1])
# print(a8[:, 1:])
# print(a8[:, -1:])
# print(a8.reshape(6,2))
# print(a8.reshape(3,4))

# print(np.zeros((4,3)))
# print(np.random.randn(4))  #1D array
# print(np.random.rand(3,3))  #2D array
# print(np.random.randint(low=1, high=10, size=(3,3)))  #2D array of ints in range