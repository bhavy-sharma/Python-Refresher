import numpy as np

# arr = np.array(42)    # 0-D array

# arr1 = np.array([1,2,3,4,5])  # 1D array

# arr2 = np.array([[1,2,3], [1,2,3]])  # 2D array

# arr3 = np.array([[[1,2,3], [4,5,6]], [[1,2,3], [4,5,6]]])  # 3D array

# print(arr.ndim)
# print(arr1.ndim)
# print(arr2.ndim)
# print(arr3.ndim)


arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print("Number of DImension is ", arr.ndim)