import pandas as pd



df = pd.read_csv("../teststr.csv")


# 1.获取Series的str属性，使用各种字符串处理函数
df["amount_type"].str

# df["amount_type"].str.replace("数据", "")


# 判断是不是数字
df["amount_type"].str.isnumeric()

# print(df["amount_type"].map(str).str.len())

# 2、使用str的startswith、contains等得到bool的Series可以做条件查询


condition = df["update_time"].str.startswith("2023-01-10 00:01:00")

# df[condition].head()

# 3、需要多次str处理的链式操作

# print(df["update_time"].str.replace("-", ""))
#
# # 每次调用函数，都返回一个新Series
# print(df["update_time"].str.replace("-", "")[:6])
#
# # slice就是切片语法，可以直接用
# print(df["update_time"].str.replace("-", "").str[0:8])


# 4. 使用正则表达式的处理
# 添加新列
# def get_nianyueri(x):
#     year, month, day = x["update_time"].split("-")[:3]
#     return f"{year}年{month}月{day}日"
#
# df["中文日期"] = df.apply(get_nianyueri, axis=1)
#
# # 方法1：链式replace
# print(df["中文日期"].str.replace("年", "").str.replace("月", "").str.replace("日", ""))
#
# # 方法2：正则表达式替换
# print(df["中文日期"].str.replace("[年月日]", ""))

# 4. 添加新列，格式化中文日期
def get_nianyueri(x):
    date, time = x["update_time"].split(" ")
    year, month, day = date[:4], date[4:6], date[6:8]
    return f"{year}年{month}月{day}日 {time}"

df["中文日期"] = df.apply(get_nianyueri, axis=1)

# 打印结果
print(df["中文日期"].head())


