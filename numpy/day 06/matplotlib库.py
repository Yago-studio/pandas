# 导入包
import numpy as np
import matplotlib.pyplot as plt
# # 生成横轴数据
# x_array = np.linspace(0, 2*np.pi, 100)
# # 正弦函数数据
# sin_y = np.sin(x_array)
# # 余弦函数数据
# cos_y = np.cos(x_array)
# # 设置图片大小
# fig, ax = plt.subplots(figsize=(8, 6))
# # 绘制正弦和余弦曲线
# ax.plot(x_array, sin_y,
# label='sin', color='b', linewidth=2)
# ax.plot(x_array, cos_y,
# label='cos', color='r', linewidth=2)
# # 设置标题、横轴和纵轴标签
# ax.set_title('Sine and cosine functions')
# ax.set_xlabel('x')
# ax.set_ylabel('f(x)')
# # 添加图例
# ax.legend()
# # 设置横轴和纵轴范围
# ax.set_xlim(0, 2*np.pi)
# ax.set_ylim(-1.5, 1.5)
# # 设置横轴标签和刻度标签
# x_ticks = np.arange(0, 2*np.pi+np.pi/2, np.pi/2)
# x_ticklabels = [r'$0$', r'$\frac{\pi}{2}$',
# r'$\pi$', r'$\frac{3\pi}{2}$',
# r'$2\pi$']
# ax.set_xticks(x_ticks)
# ax.set_xticklabels(x_ticklabels)
# # 横纵轴采用相同的scale
# ax.set_aspect('equal')
# plt.grid()
# # 将图片存成SVG格式
# plt.savefig('正弦_余弦函数曲线.png', format='png')
# # 显示图形
# plt.show()
#
# x = np.linspace(0, 2*np.pi, 100)
# y = np.sin(x)
# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1)
# ax.plot(x, y)
# plt.show()

#多个图在同一列表显示
x = np.linspace(0, 2 * np.pi, 100)
y_sin = np.sin(x)
y_cos = np.cos(x)
# 创建图形对象和子图布局
fig, (ax1, ax2) = plt.subplots(1, 2,
figsize=(10, 4),
sharey=True)
# 在左子图中绘制正弦函数曲线，设置为蓝色
ax1.plot(x, y_sin, color='blue')
ax1.set_title('Sine function')
ax1.set_xlabel('x')
ax1.set_ylabel('f(x)',
rotation='horizontal',
ha='right')
# x_ticks = np.arange(0, 2*np.pi+np.pi/2, np.pi/2) 生成横轴刻度的位置，从 0 到2π，间隔为 π/2。
# ► x_ticklabels = [r'$0$', r'$\frac{\pi}{2}$', r'$\pi$',r'$\frac{3\pi}{2}$',
# r'$2\pi$'] 设置横轴刻度的标签，分别为 0, π/2, π, 3π/2,
# 2π。在代码中，r'$\frac{\pi}{2}$' 是一个特殊的字符串，用于表示数学公式中的文本。在
# 这个字符串前面的 r 前缀表示该字符串是一个“原始字符串”，即不对字符串中的特殊字符进行转
# 义。
# ► 在这个特殊字符串中，使用了 LaTeX 符号来表示一个分数。具体来说，\frac{\pi}{2} 表示
# 一个分数，分子是 π，分母是 2。当这个字符串被用作横轴刻度的标签时，它会在图表中显示为
# "π/2" 的形式。这种表示方法可以用于在图表中显示复杂的数学公式或符号。
ax1.set_xlim(0, 2*np.pi)
ax1.set_ylim(-1.5, 1.5)
x_ticks = np.arange(0, 2*np.pi+np.pi/2, np.pi)
x_ticklabels = [r'$0$', r'$\pi$', r'$2\pi$']
ax1.set_xticks(x_ticks)
ax1.set_xticklabels(x_ticklabels)
ax1.grid(True)
ax1.set_aspect('equal')
# 在右子图中绘制余弦函数曲线，设置为红色
ax2.plot(x, y_cos, color='red')
ax2.set_title('Cosine function')
ax2.set_xlabel('x')
ax2.set_ylabel('f(x)',
rotation='horizontal',
ha='right')
ax2.set_xlim(0, 2*np.pi)
ax2.set_ylim(-1.5, 1.5)
ax2.set_xticks(x_ticks)
ax2.set_xticklabels(x_ticklabels)
ax2.grid(True)
ax2.set_aspect('equal')
# 调整子图之间的间距
plt.tight_layout()
# 显示图形
plt.show()

