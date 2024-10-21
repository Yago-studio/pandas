# 主成分分析
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import pandas_datareader as pdr
# 需要先安装库 pip install pandas_datareader
import seaborn as sns
# 下载数据，两个 tenors
df = pdr.data.DataReader(['DGS6MO', 'DGS1'],
data_source='fred',
start='01-01-2022',
end='12-31-2022')
df = df.dropna()
# 修改数据帧的column names
df = df.rename(columns={'DGS6MO': 'X1',
'DGS1': 'X2'})

# 计算日收益率
X_df = df.pct_change()
# 删除缺失值
X_df = X_df.dropna()
# 数据标准化
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_df)

from sklearn.covariance import EmpiricalCovariance
x1_array = np.linspace(-6, 6, 601)
x2_array = np.linspace(-6, 6, 601)
xx1, xx2 = np.meshgrid(x1_array, x2_array)

xx12 = np.c_[xx1.ravel(), xx2.ravel()]
# 加载学习样本数据
COV = EmpiricalCovariance().fit(X_scaled)
# 计算网格化数据的马氏距离
mahal_sq_Xc = COV.mahalanobis(xx12)
mahal_sq_dd = mahal_sq_Xc.reshape(xx1.shape)
mahal_dd = np.sqrt(mahal_sq_dd)
fig, ax = plt.subplots()
# 绘制马氏距离填充等高线
plt.contourf(xx1, xx2, mahal_dd,
cmap='Blues_r', levels=np.linspace(0,6,13))
# 绘制样本数据 (标准化) 散点图
plt.scatter(X_scaled[:,0],X_scaled[:,1],
s = 38, edgecolor = 'w', alpha=0.5,
marker='.', color='k')
# 绘制样本数据质心
plt.plot(X_scaled[:,0].mean(),X_scaled[:,1].mean(),
marker='x', color='k', markersize = 18)
ax.axvline(x = 0, c = 'k'); ax.axhline(y = 0, c = 'k')
ax.grid('off'); ax.set_aspect('equal', adjustable='box')
ax.set_xbound(lower = -6, upper = 6)
ax.set_ybound(lower = -6, upper = 6)

plt.show()
