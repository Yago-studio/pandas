
# 计算两点欧氏距离
import matplotlib.pyplot as plt
import itertools
import numpy as np
import matplotlib as mpl
import seaborn as sns
import string
from scipy.spatial import distance_matrix
from scipy.spatial.distance import euclidean
import os
# 如果文件夹不存在，创建文件夹
if not os.path.isdir("Figures"):
    os.makedirs("Figures")
# 产生随机数
num = 26
np.random.seed(0)
data = np.random.randint(10 + 1, size=(num, 2))
labels = list(string.ascii_uppercase)
cmap = mpl.cm.get_cmap('RdYlBu_r')
fig, ax = plt.subplots()
# 绘制成对线段
for i, d in enumerate(itertools.combinations(data, 2)):
    d_idx = euclidean(d[0],d[1])
    plt.plot([d[0][0],d[1][0]],
     [d[0][1],d[1][1]],
     color = cmap(d_idx/np.sqrt(2)/10),lw = 1)
ax.scatter(data[:,0],data[:,1],
marker = 'x',color = 'k',s = 50,zorder=100)
# 添加标签
for i, txt in enumerate(labels):
     ax.annotate(txt,(data[i,0] + 0.2, data[i,1] + 0.2))
ax.set_xlim(0, 10); ax.set_ylim(0, 10)
ax.set_xticks(np.arange(11))
ax.set_yticks(np.arange(11))
plt.xlabel('x'); plt.ylabel('y')
ax.grid(ls='--',lw=0.25,color=[0.5,0.5,0.5])
ax.set_aspect('equal', adjustable='box')
# fig.savefig('Figures/成对距离连线.svg', format='svg')
# 计算成对距离矩阵
pairwise_distances = distance_matrix(data, data)
fig, ax = plt.subplots()
sns.heatmap(pairwise_distances,
cmap = 'RdYlBu_r', square = True,
xticklabels = labels,yticklabels = labels,
ax = ax)
plt.show()
# fig.savefig('Figures/成对距离矩阵热图.svg', format='svg')


#插值
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
# 生成随数据
np.random.seed(8)
x = np.linspace(0, 10, 10)
y = np.random.rand(10) * 10
x_fine = np.linspace(0, 10, 1001)
# 创建一个图形对象，包含六个子图
fig, axes = plt.subplots(2, 3, figsize=(6, 9),
sharex = 'col',
sharey = 'row')
axes = axes.flatten()
# 六种插值方法
methods = ['linear','quadratic','cubic',
'previous','next','nearest']
for i, method in enumerate(methods):
# 创建 interp1d 对象
    f = interp1d(x, y, kind=method)
# 生成插值后的新数据点
    y_fine = f(x_fine)
# 绘制子图
    axes[i].plot(x, y, 'o', label='Data',
    markeredgewidth=1.5,
    markeredgecolor = 'w',
    zorder = 100)
    axes[i].plot(x_fine,y_fine,label='Interpolated')
    axes[i].set_title(f'Method: {method}')
    axes[i].legend()
    axes[i].set_xlim(0, 10)
    axes[i].set_ylim(0, 10)
    axes[i].set_aspect('equal', adjustable='box')
plt.tight_layout()
# fig.savefig('不同插值方法.svg', format='svg')
plt.show()

# 高斯分布
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from scipy.stats import norm
x_array = np.linspace(-6, 6, 200)
mu_array = np.linspace(-4, 4, 9)
# 设定均值一系列取值
colors = cm.RdYlBu(np.linspace(0,1,len(mu_array)))
# 均值对一元高斯分布PDF影响
fig, ax = plt.subplots(figsize = (5,4))
for idx, mu_idx in enumerate(mu_array):
      pdf_idx = norm.pdf(x_array,scale = 1,loc = mu_idx)
      legend_idx = '$\mu$ = ' + str(mu_idx)
      plt.plot(x_array, pdf_idx,
              color=colors[idx],
              label = legend_idx)
plt.legend(ncol=3)
ax.set_xlim(x_array.min(),x_array.max())
ax.set_ylim(0,1)
ax.set_xlabel('x')
ax.set_ylabel('PDF, $f_X(x)$')
sigma_array = np.linspace(0.5,5,10)
# 设定标准差一系列取值
colors = cm.RdYlBu(np.linspace(0,1,len(sigma_array)))
# 标准差对一元高斯分布PDF影响
fig, ax = plt.subplots(figsize = (5,4))
for idx, sigma_idx in enumerate(sigma_array):
     pdf_idx = norm.pdf(x_array, scale = sigma_idx)
     legend_idx = '$\sigma$ = ' + str(sigma_idx)
     plt.plot(x_array, pdf_idx,
             color=colors[idx],
             label = legend_idx)
plt.legend()
ax.set_xlim(x_array.min(),x_array.max())
ax.set_ylim(0,1)
ax.set_xlabel('x')
ax.set_ylabel('PDF, $f_X(x)$')
plt.show()
