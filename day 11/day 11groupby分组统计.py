import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
                   'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
                   'C': np.random.randn(8),
                   'D': np.random.randn(8)})

# 一、分组使用聚合函数做数据统计
print(df.groupby('B').sum())

df.groupby(['A', 'B']).mean()

df.groupby(['A','B'], as_index=False).mean()


# 3、同时查看多种数据统计

df.groupby('A')[["C", "D"]].agg(["sum", "mean", "std"])

# 方法1：预过滤，性能更好
df.groupby('A')['C'].agg(["sum", "mean", "std"])

# 方法2
df.groupby('A')[["C", "D"]].agg(["sum", "mean", "std"])['C']

# 5、不同列使用不同的聚合函数
df.groupby('A').agg({"C": "sum", "D": "mean"})

# 二、遍历groupby的结果理解执行流程
# 1、遍历单个列聚合的分组

g = df.groupby('A')


for name, group in g:
    print(name)
    print(group)
    print()

# 2、遍历多个列聚合的分组
g.get_group('bar')

for name, group in g:
    print(name)
    print(group)
    print()

g.get_group(('foo', 'one'))


g['C']


for name, group in g['C']:
    print(name)
    print(group)
    print(type(group))
    print()

# 三、实例分组探索天气数据


df['month'] = df['ymd'].str[:7]
df.head()

# 1、查看每个月的最高温度
data = df.groupby('month')['bWendu'].max()


data.plot()
# 2、查看每个月的最高温度、最低温度、平均空气质量指数
group_data = df.groupby('month').agg({"bWendu":"max", "yWendu":"min", "aqi":"mean"})

group_data.plot()
