# 导入包
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
# 加载鸢尾花数据集
iris = datasets.load_iris()
# 取出前三个特征作为横纵坐标和高度
X = iris.data[:, :3]
y = iris.target
# 创建3D图像对象
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# 绘制散点图
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=y)
# 设置坐标轴标签
ax.set_xlabel('Sepal length')
ax.set_ylabel('Sepal width')
ax.set_zlabel('Petal length')
# 设置坐标轴取值范围
ax.set_xlim(4,8); ax.set_ylim(1,5); ax.set_zlim(0,8)
# 设置正交投影
ax.set_proj_type('ortho')
# 显示图像
plt.show()


import plotly.express as px
# 导入鸢尾花数据
df = px.data.iris()
fig = px.scatter_3d(df,
x='sepal_length',
y='sepal_width',
z='petal_length',
size = 'petal_width',
color='species')
fig.update_layout(autosize=False,width=500,height=500)
fig.layout.scene.camera.projection.type = "orthographic"
fig.show()

#线图
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
# 生成随机游走数据
num_steps = 300
t = np.arange(num_steps)
x = np.cumsum(np.random.standard_normal(num_steps))
y = np.cumsum(np.random.standard_normal(num_steps))
z = np.cumsum(np.random.standard_normal(num_steps))
# 用 Matplotlib 可视化
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x,y,z,color = 'darkblue')
ax.scatter(x,y,z,c = t, cmap = 'viridis')
ax.set_xticks([]); ax.set_yticks([]); ax.set_zticks([])
# 设置正交投影
ax.set_proj_type('ortho')
# 设置相机视角
ax.view_init(elev = 30, azim = 120)
# 显示图像
plt.show()
# 用 Plotly 可视化
fig = go.Figure(data=go.Scatter3d(
x=x, y=y, z=z,
marker=dict(size=4,color=t,colorscale='Viridis'),
line=dict(color='darkblue', width=2)))
fig.layout.scene.camera.projection.type = "orthographic"
fig.update_layout(width=800,height=700)
fig.show() # 显示绘图结果

#网格面
# 导入包
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
# 生成曲面数据
x1_array = np.linspace(-3,3,121)
x2_array = np.linspace(-3,3,121)
xx1, xx2 = np.meshgrid(x1_array, x2_array)
ff = xx1 * np.exp(- xx1**2 - xx2 **2)
# 用 Matplotlib 可视化三维曲面
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(xx1, xx2, ff, cmap='RdYlBu_r')
# 设置坐标轴标签
ax.set_xlabel('x1'); ax.set_ylabel('x2');
ax.set_zlabel('f(x1,x2)')
# 设置坐标轴取值范围
ax.set_xlim(-3,3); ax.set_ylim(-3,3); ax.set_zlim(-0.5,0.5)
# 设置正交投影
ax.set_proj_type('ortho')
# 设置相机视角
ax.view_init(elev = 30, azim = 150)
plt.tight_layout()
plt.show()
# 用 Plotly 可视化三维曲面
fig = go.Figure(data=[go.Surface(z=ff, x=xx1, y=xx2,
colorscale='RdYlBu_r')])
fig.layout.scene.camera.projection.type = "orthographic"
fig.update_layout(width=800,height=700)
fig.show()

#三维等高线
# 导入包
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
# 生成曲面数据
x1_array = np.linspace(-3,3,121)
x2_array = np.linspace(-3,3,121)
xx1, xx2 = np.meshgrid(x1_array, x2_array)
ff = xx1 * np.exp(- xx1**2 - xx2 **2)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.contour(xx1, xx2, ff, cmap='RdYlBu_r', levels = 20)
# 设置坐标轴标签
ax.set_xlabel('x1'); ax.set_ylabel('x2'); ax.set_zlabel('f(x1,x2)')
# 设置坐标轴取值范围
ax.set_xlim(-3,3); ax.set_ylim(-3,3); ax.set_zlim(-0.5,0.5)
# 设置正交投影
ax.set_proj_type('ortho')
# 设置相机视角
ax.view_init(elev = 30, azim = 150)
plt.tight_layout()
plt.show()
contour_settings = {"z": {"show":True,"start":-0.5,
"end":0.5, "size": 0.05}}
fig = go.Figure(data=[go.Surface(x=xx1,y=xx2,z=ff,
colorscale='RdYlBu_r',
contours = contour_settings)])
fig.layout.scene.camera.projection.type = "orthographic"
fig.update_layout(width=800, height=700)
fig.show() # 显示绘图结果

#箭头图
# 导入包
import matplotlib.pyplot as plt
# 定义二维列表
A = [[0,5],[3,4],[5,0]]
# 自定义可视化函数
def draw_vector(vector,RBG):
     plt.quiver(0, 0, vector[0], vector[1],angles='xy',
              scale_units='xy',scale=1,color = RBG,
               zorder = 1e5)
fig, ax = plt.subplots()
v1 = A[0] # 第一行向量
draw_vector(v1,'#FFC000')
v2 = A[1] # 第二行向量
draw_vector(v2,'#00CC00')
v3 = A[2] # 第三行向量
draw_vector(v3,'#33A8FF')
ax.axvline(x = 0, c = 'k')
ax.axhline(y = 0, c = 'k')
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.grid()
ax.set_aspect('equal', adjustable='box')
ax.set_xbound(lower = -0.5, upper = 5)
ax.set_ybound(lower = -0.5, upper = 5)
plt.show()