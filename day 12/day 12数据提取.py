import pandas as pd


stock_info_path = "E:\\数据集\\nasdaq100\\nasdaq100\\full\\stock_name.txt"

# 使用python引擎读取

df_stock_info1 = pd.read_csv(stock_info_path, sep=' - ', nrows=50,
                             names=['公司简称', '公司英文全称', '公司中文名称', '业务范围'],
                             engine='python')
df_stock_info2 = pd.read_csv(stock_info_path, sep=' - ', header=50,
                             names=['公司简称', '公司英文全称', '公司中文名称', '业务范围'],
                             engine='python')

# 清理数据
df_stock_info1["公司简称"] = df_stock_info1["公司简称"].str.replace(".", " ", regex=False)
df_stock_info1["公司英文全称"] = df_stock_info1["公司英文全称"].str.replace(",", "").str.replace(".", " ", regex=False)

# 不需要循环，直接清理所有数字
df_stock_info1["公司简称"] = df_stock_info1["公司简称"].str.replace(r'\d+', " ", regex=True)

# 对df_stock_info2进行类似的处理
df_stock_info2["公司简称"] = df_stock_info2["公司简称"].str.replace(".", "", regex=False)
df_stock_info2["公司英文全称"] = df_stock_info2["公司英文全称"].str.replace(",", "").str.replace(".", " ", regex=False)
df_stock_info2["公司简称"] = df_stock_info2["公司简称"].str.replace(r'\d+', " ", regex=True)

# 交换两个列的值
df_stock_info2[['公司中文名称', '公司英文全称']] = df_stock_info2[['公司英文全称', '公司中文名称']].values

df_stock_total = pd.concat([df_stock_info1, df_stock_info2])

df_stock_total.to_excel("stockInfo.xlsx", index=False)
