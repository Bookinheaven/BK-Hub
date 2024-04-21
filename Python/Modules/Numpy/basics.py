import numpy as np

arr = np.array([1,2,3,4,5])
print(arr)
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)
a = np.array(42, ndmin=10)
b = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a,a.ndim)
print(b.ndim)
print(arr[1, 1])
print(arr[1, 1:4])