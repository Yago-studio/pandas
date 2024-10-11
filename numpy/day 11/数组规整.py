import numpy as np

arr = np.random.random(12)

arr = np.reshape(arr, (2, 3, 2))

print(arr)


a = np.array([[1, 2], [3, 4]])
b = np.reshape(a, -1)  #将二维数组展开为一维数组

print(b)

a = np.arange(6).reshape((2, 3)) #a = np.arange(6).reshape((2, 3)) #创建一个 2行 3列的二维数组
b = np.reshape(a, (3, 2), order='F')
b = np.reshape(a, (3, 2), order='F')

# 线性代数


