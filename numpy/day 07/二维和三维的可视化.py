# 导入包
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import numpy as np
# 加载鸢尾花数据集
# iris = load_iris()
# # 提取花萼长度和花萼宽度作为变量
# sepal_length = iris.data[:, 0]
# sepal_width = iris.data[:, 1]
# target = iris.target
# fig, ax = plt.subplots()
# # 创建散点图
# plt.scatter(sepal_length, sepal_width, c=target, cmap='rainbow')
# # 添加标题和轴标签
# plt.title('Iris sepal length vs width')
# plt.xlabel('Sepal length (cm)')
# plt.ylabel('Sepal width (cm)')
# # 设置横纵轴刻度
# # ax.set_xticks(np.arange(4, 8 + 1, step=1))
# # ax.set_yticks(np.arange(1, 5 + 1, step=1))
# # 设定横纵轴尺度1:1
# ax.axis('scaled')
# # 增加刻度网格，颜色为浅灰
# ax.grid(ls='--', lw=0.25, c=[0.7,0.7,0.7])
# # 设置横纵轴范围
# ax.set_xbound(lower = 4, upper = 8)
# ax.set_ybound(lower = 1, upper = 5)
# # 显示图形
# plt.show()
#
# import plotly.express as px
# # 从Ploly中导入鸢尾花样本数据
# iris_df = px.data.iris()
# # 绘制散点图，不渲染marker
# fig = px.scatter(iris_df, x="sepal_length", y="sepal_width",
# width = 600, height = 600,
# labels={"sepal_length": "Sepal length (cm)",
# "sepal_width": "Sepal width (cm)"})
# # 修饰图像
# fig.update_layout(xaxis_range=[4, 8], yaxis_range=[1, 5])
# xticks = np.arange(4,8+1)
# yticks = np.arange(1,5+1)
# fig.update_layout(xaxis = dict(tickmode = 'array',
# tickvals = xticks))
# fig.update_layout(yaxis = dict(tickmode = 'array',
# tickvals = yticks))
# fig.show()
# # 绘制散点图，渲染marker展示鸢尾花分类
# fig = px.scatter(iris_df, x="sepal_length", y="sepal_width",
# color="species",
# width = 600, height = 600,
# labels={"sepal_length": "Sepal length (cm)",
# "sepal_width": "Sepal width (cm)"})
# # 修饰图像
# fig.update_layout(xaxis_range=[4, 8], yaxis_range=[1, 5])
# fig.update_layout(xaxis = dict(tickmode = 'array',
# tickvals = xticks))
# fig.update_layout(yaxis = dict(tickmode = 'array',
# tickvals = yticks))
# fig.update_layout(legend=dict(yanchor="top", y=0.99,
# xanchor="left",x=0.01))
# fig.show()


#等高线
#
# #创建二维数据
# x = np.linspace(-2, 2, 100)
# y = np.linspace(-2, 2, 100)
# X, Y = np.meshgrid(x, y)
# Z = X**2 + Y**2
#
# #绘制等高线图
# plt.contour(X, Y, Z, levels=np.linspace(0, 8, 16 + 1), cmap='RdYlBu_r')
# #添加颜色图例
# plt.colorbar()
# #显示图形
# plt.show()
#
# x1_array = np.linspace(-3,3,121)
# x2_array = np.linspace(-3,3,121)
# xx1, xx2 = np.meshgrid(x1_array, x2_array)
# ff = xx1 * np.exp(- xx1**2 - xx2 **2)
#
# fig, ax = plt.subplots()
# CS = ax.contour(xx1, xx2, ff, levels = 20,
# cmap = 'RdYlBu_r', linewidths = 1)
# fig.colorbar(CS)
# ax.set_xlabel('$\it{x_1}$'); ax.set_ylabel('$\it{x_2}$')
# ax.set_xticks([])
# ax.set_yticks([])
# ax.set_xlim(xx1.min(), xx1.max())
# ax.set_ylim(xx2.min(), xx2.max())
# ax.grid(False)
# ax.set_aspect('equal', adjustable='box')
# # 填充等高线
# fig, ax = plt.subplots()
# CS = ax.contourf(xx1, xx2, ff, levels = 20,
# cmap = 'RdYlBu_r')
# fig.colorbar(CS)
# ax.set_xlabel('$\it{x_1}$'); ax.set_ylabel('$\it{x_2}$')
# ax.set_xticks([]); ax.set_yticks([])
# ax.set_xlim(xx1.min(), xx1.max())
# ax.set_ylim(xx2.min(), xx2.max())
# ax.grid(False)
# ax.set_aspect('equal', adjustable='box')
# plt.show()



# import plotly.graph_objects as go
# # 生成数据
# x1_array = np.linspace(-3,3,121)
# x2_array = np.linspace(-3,3,121)
# xx1, xx2 = np.meshgrid(x1_array, x2_array)
# ff = xx1 * np.exp(- xx1**2 - xx2 **2)
# # 等高线设置
# levels = dict(start=-0.5,end=0.5,size=0.05)
# data = go.Contour(x=x1_array,y=x2_array,z=ff,
# contours_coloring='lines',
# line_width=2,
# colorscale = 'RdYlBu_r',
# contours=levels)
# # 创建布局
# layout = go.Layout(
# width=600, # 设置图形宽度
# height=600, # 设置图形高度
# xaxis=dict(title=r'$x_1$'),
# yaxis=dict(title=r'$x_2$'))
# # 创建图形对象
# fig = go.Figure(data=data, layout=layout)
# fig.show()

#热图
import seaborn as sns
#创建二维数据
iris_sns = sns.load_dataset("iris")
# 绘制热图
fig, ax = plt.subplots()
sns.heatmap(data=iris_sns.iloc[:,0:-1],
vmin = 0, vmax = 8,
ax = ax,
yticklabels = False,
xticklabels = ['Sepal length', 'Sepal width',
'Petal length', 'Petal width'],
cmap = 'RdYlBu_r')
plt.show()

import plotly.express as px
# 从Plotly中导入鸢尾花样本数据
df = px.data.iris()
# 创建Plotly热图
fig = px.imshow(df.iloc[:,0:-2], text_auto=False,
width = 600, height = 600,
x = None, zmin=0, zmax=8,
color_continuous_scale = 'viridis')
# 隐藏 y 轴刻度标签
fig.update_layout(yaxis=dict(tickmode='array',tickvals=[]))
# 修改 x 轴刻度标签
x_labels = ['Sepal length', 'Sepal width',
'Petal length', 'Petal width']
x_ticks = list(range(len(x_labels)))
fig.update_xaxes(tickmode='array',tickvals=x_ticks,
ticktext=x_labels)
fig.show()
