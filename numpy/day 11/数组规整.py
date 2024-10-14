
import seaborn as sns
import numpy as np
from matplotlib import pyplot as plt


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
X = np.linspace(2, 20, 100).reshape(10, 10)


G = X.T @ X
# 第二个格拉姆矩阵
H = X @ X.T
# 可视化第一个格拉姆矩阵运算
fig,axs = plt.subplots(1,5,figsize = (8,3),
gridspec_kw={'width_ratios':
[3, 0.5, 3, 0.5, 3]})
# 图形状态切换到第1幅子图
plt.sca(axs[0])
# 绘制格拉姆矩阵
ax = sns.heatmap(G, cmap = 'RdYlBu_r',
vmax = 5000, vmin = 0,
annot = False,
fmt=".0f",
cbar_kws = {'orientation':'horizontal'},
xticklabels = False,
yticklabels=False,
square = 'equal')
plt.title('$G$')
# 图形状态切换到第2幅子图
plt.sca(axs[1])
plt.title('=')
plt.axis('off')
# 图形状态切换到第3幅子图
plt.sca(axs[2])
# 绘制X转置
ax = sns.heatmap(X.T, cmap = 'RdYlBu_r',
vmax = 0, vmin = 8,
cbar_kws = {'orientation':'horizontal'},
xticklabels = False,
yticklabels = False,
annot=False)
plt.title('$X^T$')
# 图形状态切换到第4幅子图
plt.sca(axs[3])
plt.title('@')
plt.axis('off')
# 图形状态切换到第5幅子图
plt.sca(axs[4])
# 绘制X
ax = sns.heatmap(X, cmap = 'RdYlBu_r',
vmax = 0, vmin = 8,
cbar_kws = {'orientation':'horizontal'},
xticklabels = False,
yticklabels=False,
annot=False)
plt.title('$X$')

plt.show()
