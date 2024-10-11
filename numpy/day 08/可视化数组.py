import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import math
from matplotlib import cm
# 定义二维数组可视化函数
def visualize_2D(array, title, vmax, vmin):
  fig_width = math.ceil(array.shape[1] * 0.5)
  fig_length = math.ceil(array.shape[0] * 0.5)
  fig, ax = plt.subplots(figsize=(fig_width, fig_length))
  sns.heatmap(array,
  vmax = vmax,
  vmin = vmin,
  annot = True, # 增加注释
  fmt = ".0f", # 注释数值的格式
  square = True, # 热图方格为正方形
  cmap = 'RdYlBu_r', # 指定色谱
  linewidths = .5, # 方格线宽
  cbar = False, # 不显示色谱条
  yticklabels=False, # 不显示纵轴标签
  xticklabels=False, # 不显示横轴标签
  ax = ax) # 指定绘制热图的轴
  plt.show()

# 定义一维数组可视化函数
def visualize_1D(array, title):
  fig, ax = plt.subplots()
  colors = cm.RdYlBu_r(np.linspace(0,1,len(array)))
  for idx in range(len(array)):
    circle_idx = plt.Circle((idx, 0), 0.5,
    facecolor=colors[idx],
    edgecolor = 'w')
    ax.add_patch(circle_idx)
    ax.text(idx, 0, s = str(array[idx]),
         horizontalalignment = 'center',
         verticalalignment = 'center')
  ax.set_xlim(-0.6, 0.6 + len(array))
  ax.set_ylim(-0.6, 0.6)
  ax.set_aspect('equal', adjustable='box')
  ax.axis('off')
  plt.show()


#
# # 定义一维数组
# a_1D = np.array([-3, -2, -1, 0, 1, 2, 3])
# print(a_1D)
# print(a_1D.shape)
# print(len(a_1D))
# print(a_1D.ndim)
# print(a_1D.size)
# # 可视化
# visualize_1D(a_1D, '手动，一维')
#
# # 定义二维数组
# a_2D = np.array([[-3, -2, -1],
# [0, 1, 2]])
# print(a_2D)
# # 可视化
# visualize_2D(a_2D, '手动，二维', 3, -3)
# print(a_2D.shape)
# print(a_2D.shape[0]) # 行数
# print(a_2D.shape[1]) # 列数
# print(a_2D.ndim)
# print(a_2D.size)
# print(len(a_2D))
#
# a_row_vector = np.array([[-3, -2, -1, 0, 1, 2, 3]])
# # 可视化
# visualize_2D(a_row_vector, '手动，行向量', 3, -3)
# print(a_row_vector.shape)
# print(a_row_vector.ndim)

# 定义三维数组
a_3D = np.array([[[-12, -11, -10, -9],
[-8, -7, -6, -5],
[-4, -3, -2, -1]],
[[0, 1, 2, 3],
[4, 5, 6, 7],
[8, 9, 10, 11]]])
print(a_3D.shape)
print(a_3D.ndim)
# 可视化
visualize_2D(a_3D[0], '手动，三维，第一页', 12, -12)
print(a_3D[0].shape)
visualize_2D(a_3D[1], '手动，三维，第二页', 12, -12)