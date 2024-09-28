import pandas as pd

df = pd.read_csv("../../test.csv")

# 1、使用index查询数据
# drop==False，让索引列还保持在column
df.set_index("id", inplace=True, drop=False)

# print(df.index)

# 使用index的查询方法
# print(df.loc[500].head(5))

#2. 使用index会提升查询性能

# 将数据随机打散
from sklearn.utils import shuffle
import timeit

df_shuffle = shuffle(df)

# print(df_shuffle.index.is_unique)


# 计时，查询id==500数据性能
# def square_numbers(n):
#     return df_shuffle.loc[n]
#
# def square_origin(n):
#     return df.loc[n]
#
# timer = timeit.Timer('square_numbers(100)', 'from __main__ import square_numbers')
# execution_time = timer.timeit()
# print(f"代码的执行时间为：{execution_time} 秒")
#
# timer = timeit.Timer('square_origin(100)', 'from __main__ import square_origin')
# execution_time = timer.timeit()
# print(f"代码的执行时间为：{execution_time} 秒")


# 3. 使用index能自动对齐数据
s1 = pd.Series([1, 2, 3], index=list("abc"))

s2 = pd.Series([2, 3, 4], index=list("bcd"))

print(s1 + s2)
