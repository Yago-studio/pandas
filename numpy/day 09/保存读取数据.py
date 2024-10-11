import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from numpy import genfromtxt
# 导入鸢尾花数据
iris = load_iris()
# 将numpy array存成CSV文件
np.savetxt("Iris_data.csv", iris.data, delimiter=",")
# 将 CSV 文件读入存成numpy array
Iris_Data_array = genfromtxt('Iris_data.csv', delimiter=',')
# 可视化
fig, ax = plt.subplots(figsize = (5,5))
sns.heatmap(Iris_Data_array, # 鸢尾花数据数组
cmap = 'RdYlBu_r', # 指定色谱
ax = ax, # 指定轴
vmax = 8, # 色谱最大值
vmin = 0, # 色谱最小值
xticklabels = [], # 不显示横轴标签
yticklabels = [], # 不显示纵轴标签
cbar = True)
plt.show()