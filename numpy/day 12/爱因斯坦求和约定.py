# 导入包
import numpy as np
from sklearn.datasets import load_iris
# 从sklearn导入鸢尾花数据
iris = load_iris()
X = iris.data
y = iris.target
# 每一列求和
print(np.einsum('ij->j',X))
# np.sum(X, axis = 0)
# 每一行求和
print(np.einsum('ij->i', X))
# np.sum(X, axis = 1)
# 矩阵所有元素求和
print(np.einsum('ij->', X))
# np.sum(X, axis = (0,1))

#转置
np.einsum('ij->ji', X)
# X.T
# np.transpose(X)
# 三维数组
X3D = np.stack([X[y == 0],
X[y == 1],
X[y == 2]], axis=0)
# X[y == 0]、X[y == 1] 和 X[y == 2]：这三部分代码分别从 X 中筛选出对应类别的样本。
# 假设 y 是 [0, 1, 2, 0, 1, 2]，并且 X 是相应的特征数据，那么 X[y == 0] 会返回所有属于类别 0 的样本数据，X[y == 1] 返回所有属于类别 1 的样本数据，
# X[y == 2] 返回所有属于类别 2 的样本数据。

# print(X3D)
# 三维数组转置
X3D_T = np.einsum('ijk->ikj', X3D)

# 计算矩阵乘法 X @ X.T
np.einsum('ij,kj->ik', X, X)
# np.einsum('ij,jk->ik', X, X.T)
# X @ X.T
# 计算矩阵乘法 X.T @ X
G = np.einsum('ij,ik->jk', X, X)
# np.einsum('ij,jk->ik', X.T, X)
# X.T @ X
# 三维矩阵乘法
G_3D = np.einsum('ijk,ijm->ikm', X3D, X3D)
# np.einsum('mij,mjk->mik', X3D_T, X3D)
# 矩阵乘法
