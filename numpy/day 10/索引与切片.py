import numpy as np

arr = np.arange(1, 5+1)

# print(arr)

# print(arr[::-2])
#
# print(arr[np.r_[0:3, -1]])


#视图
a = np.array([1, 2, 3, 4, 5])
# 创建一个切片视图
s = a[1:3]
# 修改视图中的数据
s[0] = 1000
# 查看原始数组
print(a) # 输出：[1 0 3 4 5]
# 创建一个整数数组索引副本
c = a[[1, 3]].copy()
# 修改副本中的数据
c[0] = 888
# 查看原始数组
print(a) # 输出：[1 0 3 4 5]
print(c)



