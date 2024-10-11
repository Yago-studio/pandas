import numpy as np
import matplotlib.pyplot as plt
# 生成随机数，服从连续均匀分布
num = 2000
X_uniform = np.random.uniform(low=-3, high=3, size=(num,2))
fig, ax = plt.subplots(figsize = (5,5))
ax.scatter(X_uniform[:,0], # 散点横轴坐标
X_uniform[:,1], # 散点纵轴坐标
s = 100, # 散点大小
marker = '.', # 散点marker样式
alpha = 0.5, # 透明度
edgecolors = 'w')# 散点边缘颜色
ax.set_aspect('equal', adjustable='box')
# 设置纵横比为 1:1，并且调整子图框来保持纵横比
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_xticks((-3,0,3))
ax.set_yticks((-3,0,3))
plt.show()

month = np.array([1,2,3,4,5])
days = np.array([31, 29, 30, 31, 30])
fig, ax = plt.subplots(figsize=(6, 6))
ax.bar(month, days, color='blue')
ax.set_title('Month')
ax.set_xlabel('Month')
ax.set_ylabel('Days')
ax.set_yticks((0, 15, 32))
plt.show()
