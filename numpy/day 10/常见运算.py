import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
# 设置 Matplotlib 使用支持中文的字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
# 导入鸢尾花数据
# iris = load_iris()
# # print(iris.data)
# iris_data_array = iris.data
# print(iris_data_array.max()) # 整个矩阵的最大值
# print(iris_data_array.max(axis = 0)) # 每列最大值
# print(np.argmax(iris_data_array, axis=0)) # 每列最大值位置
# print(iris_data_array.max(axis = 1)) # 每行最大值位置
# print(np.average(iris_data_array, axis = 0)) # 每列均值
# # 计算每一列方差
# print(np.var(iris_data_array, axis = 0))
# # 注意，NumPy中默认分母为n
# print(np.var(iris_data_array, axis = 0, ddof = 1))
# # 将分母设为n - 1
# # 计算每一列标准差
# print(np.std(iris_data_array, axis = 0))
# # 计算协方差矩阵；注意转置
# SIGMA = np.cov(iris_data_array.T, ddof = 1)
# print(SIGMA)
# # 可视化协方差矩阵
# fig, ax = plt.subplots(figsize = (5,5))
# sns.heatmap(SIGMA, cmap = 'RdYlBu_r', annot = True,
# ax = ax, fmt = ".2f", square = True,
# xticklabels = [], yticklabels = [], cbar = True)
#
#
# # 计算协方差矩阵；注意转置
# CORR = np.corrcoef(iris_data_array.T)
# print(CORR)
# fig, ax = plt.subplots(figsize = (5,5))
# sns.heatmap(CORR, cmap = 'RdYlBu_r', annot = True,
# ax = ax, fmt = ".2f", square = True,
# xticklabels = [], yticklabels = [], cbar = True)
# plt.show()


import numpy as np
import matplotlib.pyplot as plt
# 自定义可视化函数
def visualize_fx(x_array, f_array, title, step = False):
    fig, ax = plt.subplots(figsize = (5,5))
    ax.plot([-5,5],[-5,5], c = 'r', ls = '--', lw = 0.5)
    if step:
       ax.step(x_array, f_array)
    else:
       ax.plot(x_array, f_array)
    ax.set_title(title)
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.axvline(0, c = 'k')
    ax.axhline(0, c = 'k')
    ax.set_xticks(np.arange(-5, 5+1))
    ax.set_yticks(np.arange(-5, 5+1))
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    plt.grid(True)
    ax.set_aspect('equal', adjustable='box')
    plt.show()
    fig.savefig(title + '.png', format='png')

# 幂函数，p = 2
x_array = np.linspace(-5,5,1001)
f_array = np.power(x_array, 2)
visualize_fx(x_array, f_array, '幂函数_p=2')
# 反正弦函数
x_array_ = np.copy(x_array)
x_array_[(x_array_ < -1) | (x_array_ > 1)] = np.nan
f_array = np.arcsin(x_array_)
visualize_fx(x_array_, f_array, '反正弦函数')
# 正切函数
f_array = np.tan(x_array)
f_array[:-1][np.diff(f_array) < 0] = np.nan
visualize_fx(x_array, f_array, '正切函数')
# 向下取整函数
f_array = np.floor(x_array)
visualize_fx(x_array, f_array, '向下取整函数', True)
# 对数函数
x_array_ = np.copy(x_array)
x_array_[x_array_<=0] = np.nan
f_array = np.log(x_array_)
visualize_fx(x_array_, f_array, '对数函数')
