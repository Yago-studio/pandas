import numpy as np
import pandas as pd

from functools import reduce

stock_path = "E:\\数据集\\nasdaq100\\nasdaq100\\full\\full_non_padding.csv"


df_stock_name = pd.read_excel("D:\pythonTest\量化分析\day 12\stockInfo.xlsx")
df_stock = pd.read_csv(stock_path)

stock_names = df_stock.columns


avg = []

for i in range(len(stock_names)):
    stock_name = stock_names[i]
    total = np.nansum(df_stock[stock_name].values)  # 计算总和
    # print(total)
    avg.append(total / df_stock.shape[0])# 注意这里应该是行数而不是列数


df_stock_name["avg"] = avg

df_stock_name.to_excel("stockinfo_avg.xlsx")
