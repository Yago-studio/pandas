import numpy as np
import pandas as pd
import statistics
from pandas import DataFrame
import matplotlib.pyplot as plt

# 加载数据
stock_path = "E:\\数据集\\nasdaq100\\nasdaq100\\full\\full_non_padding.csv"
df_stock_name = pd.read_excel("D:\\pythonTest\\量化分析\\pandas\\day 12\\stockInfo.xlsx")
df_stock = pd.read_csv(stock_path)

stock_names = df_stock.columns

# 计算每个股票的平均值
avg = []
for stock_name in stock_names:
    total = np.nansum(df_stock[stock_name].values)  # 计算总和
    avg.append(total / df_stock.shape[0])  # 用行数计算平均值

# 将平均值添加到股票信息 DataFrame 中
df_stock_name["avg"] = avg

max_value_index = df_stock_name['avg'].idxmax()

# 删除最大值所在的行
df_stock_name = df_stock_name.drop(max_value_index)

# 计算每个业务范围的公司数量
category_stats = df_stock_name.groupby('业务范围').size()

# 计算每个业务范围的平均股票值
h_avg = []
for cate in category_stats.index:
    matched_rows = df_stock_name[df_stock_name['业务范围'] == cate]
    avg_value = statistics.mean(matched_rows['avg'])
    h_avg.append(avg_value)

# 确保 h_avg 是 Series 而不是 DataFrame
h_avg = pd.Series(h_avg, index=category_stats.index)

# 将 h_avg 添加到 category_stats 中
category_stats = pd.DataFrame({'公司数量': category_stats, 'h_avg': h_avg})

print(category_stats)
# 排序
category_stats1 = category_stats.sort_values(by='h_avg', ascending=False)


plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(category_stats1.index, category_stats1['公司数量'], color='black', label='公司数量')
ax.bar(category_stats1.index, category_stats1['h_avg'], color='gray', alpha=0.7, label='平均股票值')
ax.set_title('纳斯达克业务范围 - 公司数量与平均股票值')
ax.set_xlabel('行业')
ax.set_ylabel('数量/平均值')
plt.xticks(rotation=45)
plt.legend()
plt.show()

