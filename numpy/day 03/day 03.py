
import numpy as np

one_arr = np.array([[1, 2, 10, 20],
[3, 4, 30, 40],
[5, 6, 50, 60]])

a = np.array([[1, 2, 10, 20],
[3, 4, 30, 40],
[5, 6, 50, 60]])


# print(np.dot(one_arr, a.T))
matrix = [[i * j for j in range(1, 4)]
for i in range(1, 4)]
# print(matrix)

def linspace(start, stop, num=50, endpoint=True):
   if num < 2:
# 报错
     raise ValueError("Number of samples must be at least 2")
# 是否包括右端点
   if endpoint:
     step = (stop - start) / (num - 1)
     return [start + i * step for i in range(num)]
   else:
    step = (stop - start) / num
    return [start + i * step for i in range(num)]
# 示例用法
start = 0 # 数列起点
stop = 10 # 数列终点
num = 21 # 数列元素
endpoint = True # 数列包含 stop
# 调用自定义函数生成等差数列
values = linspace(start, stop, num, endpoint)
# print(values)


#笛卡尔积
from itertools import product

# print(list(product(one_arr,a)))


#迭代器

#不放回排列
import itertools
string = 'abc'
perms_all = itertools.permutations(string)
#perms2 = itertools.permutations(string,2)
# 返回一个可迭代对象perms，其中包含了string的所有排列方式
# 全排列
for perm_idx in perms_all:
    print(' '.join(perm_idx))

combs_all = itertools.combinations(string)

for coms_idx in combs_all:
    print(' '.join(coms_idx))

