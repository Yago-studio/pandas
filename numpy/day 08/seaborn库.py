import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
# 导入鸢尾花数据
iris_sns = sns.load_dataset("iris")
# 绘制花萼长度样本数据直方图
fig, ax = plt.subplots(figsize = (8, 6))
sns.histplot(data=iris_sns, x="sepal_length",
binwidth=0.2, ax = ax)
# 纵轴三个选择：频率、概率、概率密度
ax.axvline(x = iris_sns.sepal_length.mean(),
color = 'r', ls = '--')
plt.show()

ig, ax = plt.subplots(figsize = (8,6))
sns.histplot(data = iris_sns, x="sepal_length",
hue = 'species', binwidth=0.2, ax = ax,
element="step", stat = 'density')
plt.show()
