import pandas as pd


df = pd.read_csv("../test.csv", skiprows=0)


#1、直接赋值的方法
# 替换掉温度的后缀℃
# df["bWendu"] = df["bWendu"].str.replace("℃", "").astype('int32')
# df["yWendu"] = df["yWendu"].str.replace("℃", "").astype('int32')

# df["wencha"] = df["bWendu"] - df["yWendu"]

#2、df.apply方法
def get_amount_type(x):
    if x["total_amount"] > 3300:
        return '数据过高'
    if x["total_amount"] < 2500:
        return '数据过低'
    return '数据正常'

# 注意需要设置axis==1，这是series的index是columns
df["amount_type"] = df.apply(get_amount_type, axis=1)

# 查看温度类型的计数
print(df["amount_type"].value_counts())

#3、df.assign方法

# 可以同时添加多个新的列

# def func(x):
#     return x["yWendu"] * 9 / 5 + 32
#
# df.assign(
#     yWendu_huashi = func,
#     # 摄氏度转华氏度
#     bWendu_huashi = lambda x : x["bWendu"] * 9 / 5 + 32
# )

#4、按条件选择分组分别赋值
#按条件先选择数据，然后对这部分数据赋值新列
#高低温差大于10度，则认为温差大

# df.loc[df["bWendu"]-df["yWendu"]>10]


# # 先创建空列（这是第一种创建新列的方法）
# df['wencha_type2'] = ''
#
# df.loc[df["bWendu"]-df["yWendu"]>10, "wencha_type2"] = "温差大"
#
# df.loc[df["bWendu"]-df["yWendu"]<=10, "wencha_type2"] = "温差正常"
#
# df["wencha_type2"].value_counts()
