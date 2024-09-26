import pandas as pd

import warnings
warnings.filterwarnings('ignore')


# 一、使用pandas.concat合并数据
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3'],
                    'E': ['E0', 'E1', 'E2', 'E3']
                   })

df2 = pd.DataFrame({ 'A': ['A4', 'A5', 'A6', 'A7'],
                     'B': ['B4', 'B5', 'B6', 'B7'],
                     'C': ['C4', 'C5', 'C6', 'C7'],
                     'D': ['D4', 'D5', 'D6', 'D7'],
                     'F': ['F4', 'F5', 'F6', 'F7']
                   })


# print(pd.concat([df1, df2]))
#
# # 2、使用ignore_index=True可以忽略原来的索引
# print(pd.concat([df1, df2], ignore_index=True))
#
# # 3、使用join=inner过滤掉不匹配的列
# print(pd.concat([df1, df2], ignore_index=True, join="inner"))

# 4、使用axis=1相当于添加新列
s1 = pd.Series(list(range(4)), name="F")
pd.concat([df1, s1], axis=1)

#添加多列Series
s2 = df1.apply(lambda x: x["A"]+"_GG", axis=1)


s2.name = "G"

pd.concat([df1, s1, s2], axis=1)

# 列表是可以混合顺序的
pd.concat([s1, df1, s2], axis=1)

# 二、使用DataFrame.append按行合并数据

df1 = pd.DataFrame([[1, 2], [3, 4]], columns=list('AB'))

df2 = pd.DataFrame([[5, 6], [7, 8]], columns=list('AB'))

# 1、给1个dataframe添加另一个dataframe
# df1.append(df2)
pd.concat([df1, df2])

# df1.append(df2, ignore_index=True)
pd.concat([df1, df2], ignore_index=True)

# 3、可以一行一行的给DataFrame添加数据
# 一个空的df
df = pd.DataFrame(columns=['A'])

# for i in range(5):
    # 注意这里每次都在复制
#     df = df.append({'A': i}, ignore_index=True)
# df

# 创建一个空的数据框
df = pd.DataFrame(columns=['A'])

# 用于存储所有新行的列表
rows_to_add = []

# 在循环中收集数据
for i in range(5):
    # 将新的行字典添加到列表中
    rows_to_add.append({'A': i})

# 使用 pd.DataFrame 从列表创建新的数据框，然后使用 pd.concat 连接
df = pd.concat([df, pd.DataFrame(rows_to_add)], ignore_index=True)

# 打印结果
print(df)


# 第一个入参是一个列表，避免了多次复制
pd.concat(
    [pd.DataFrame([i], columns=['A']) for i in range(5)],
    ignore_index=True
)

