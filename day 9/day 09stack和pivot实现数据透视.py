import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv(
    "E:\数据集\ml-1m/ratings.dat",
    header=None,
    names="UserID::MovieID::Rating::Timestamp".split("::"),
    sep="::",
    engine="python"
)

df["pdate"] = pd.to_datetime(df["Timestamp"], unit='s')

# print(df.head())

# 实现数据统计
df_group = df.groupby([df["pdate"].dt.month, "Rating"])["UserID"].agg(pv=np.size)

# print(df_group.head(10))


# 2. 使用unstack实现数据二维透视
df_stack = df_group.unstack()

df_stack.plot()

# plt.show()

# 3. 使用pivot简化透视

df_reset = df_group.reset_index()
df_reset.head()

df_pivot = df_reset.pivot(columns="pdate", index="Rating", values="pv")

df_pivot.plot()

plt.show()

