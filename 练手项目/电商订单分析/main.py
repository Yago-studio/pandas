import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn

# 设置 Matplotlib 使用支持中文的字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 1.读取数据
path1 = "E:\数据集\电商订单/tmall_order_report.csv"

path2 = "E:\数据集\电商订单\日化.xlsx"

path3 = "E:\数据集\电商订单\双十一淘宝美妆数据.csv"

data = pd.read_csv(path1, encoding="utf-8")

# print(data.columns)

#2.绘制缺失值热图
# plt.figure(figsize=(10, 6))
#
# sns.heatmap(data.isna(), cbar=False, cmap='viridis', yticklabels=False)
# plt.title('数据缺失值热图')
# plt.xlabel('字段名')
# plt.ylabel('样本索引')
# plt.show()

data.columns = data.columns.str.strip()  # 列名有空格，需要处理下

# print(data[data.duplicated()].count())  #查看重复数据数量


#整体情况
result = {}
result['总订单数'] = data['订单编号'].count()
result['已完成订单数'] = data['订单编号'][data['订单付款时间'].notnull()].count()
result['未付款订单数'] = data['订单编号'][data['订单付款时间'].isnull()].count()
result['退款订单数'] = data['订单编号'][data['退款金额'] > 0].count()
result['总订单金额'] = data['总金额'][data['订单付款时间'].notnull()].sum()
result['总退款金额'] = data['退款金额'][data['订单付款时间'].notnull()].sum()
result['总实际收入金额'] = data['买家实际支付金额'][data['订单付款时间'].notnull()].sum()


# print(result)

# 可视化
from pyecharts import options as opts
from pyecharts.charts import Map, Bar, Line
from pyecharts.components import Table
from pyecharts.options import ComponentTitleOpts
from pyecharts.faker import Faker

table = Table()

headers = ['总订单数', '总订单金额', '已完成订单数', '总实际收入金额', '退款订单数', '总退款金额', '成交率', '退货率']
rows = [
    [
        result['总订单数'], f"{result['总订单金额']/10000:.2f} 万", result['已完成订单数'], f"{result['总实际收入金额']/10000:.2f} 万",
        result['退款订单数'], f"{result['总退款金额']/10000:.2f} 万",
        f"{result['已完成订单数']/result['总订单数']:.2%}",
        f"{result['退款订单数']/result['已完成订单数']:.2%}",
    ]
]
table.add(headers, rows)
table.set_global_opts(
    title_opts=ComponentTitleOpts(title='整体情况')
)
# table.render("chart.html")


# 地区分析
result2 = data[data['订单付款时间'].notnull()].groupby('收货地址').agg({'订单编号': 'count'})
# print(result2)
result21 = result2.to_dict()['订单编号']
# print(result21)

c = (
    Map()
    .add("订单量", [*result21.items()], "china", is_map_symbol_show=False)
    .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="地区分布"),
        visualmap_opts=opts.VisualMapOpts(max_=1000),
    )
)

# c.render("地区分布.html")


# 时间分析
data['订单创建时间'] = pd.to_datetime(data['订单创建时间'])
data['订单付款时间'] = pd.to_datetime(data['订单付款时间'])

result31 = data.groupby(data['订单创建时间'].apply(lambda x: x.strftime("%Y-%m-%d"))).agg({'订单编号':'count'}).to_dict()['订单编号']

c = (
    Line()
    .add_xaxis(list(result31.keys()))
    .add_yaxis("订单量", list(result31.values()))
    .set_series_opts(
        label_opts=opts.LabelOpts(is_show=False),
        markpoint_opts=opts.MarkPointOpts(
            data=[
                opts.MarkPointItem(type_="max", name="最大值"),
            ]
        ),
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="每日订单量走势"))
)
# c.render("每日订单量走势.html")

result32 = data.groupby(data['订单创建时间'].apply(lambda x: x.strftime("%H"))).agg({'订单编号':'count'}).to_dict()['订单编号']
x = [*result32.keys()]
y = [*result32.values()]
c = (
    Bar()
    .add_xaxis(x)
    .add_yaxis("订单量", y)
    .set_global_opts(title_opts=opts.TitleOpts(title="每小时订单量走势"))
    .set_series_opts(
        label_opts=opts.LabelOpts(is_show=False),
        markpoint_opts=opts.MarkPointOpts(
            data=[
                opts.MarkPointItem(type_="max", name="峰值"),
                opts.MarkPointItem(name="第二峰值", coord=[x[15], y[15]], value=y[15]),
                opts.MarkPointItem(name="第三峰值", coord=[x[10], y[10]], value=y[10]),
            ]
        ),
    )
)
# c.render("每小时订单量走势.html")

# 第二部分

data2 = pd.read_csv(path3)


# 数据清洗

data2.drop_duplicates(inplace=True) #删除重复值
data2.reset_index(drop=True, inplace=True) #重建索引
data2.isnull().sum()#查看空值，销售数量和评论数有空值
# fig = plt.figure(figsize=(6, 4))
# sns.heatmap(data2.isna(), cbar=False, cmap='viridis', yticklabels=False)
# plt.title('数据缺失值热图')
# plt.xlabel('字段名')
# plt.ylabel('样本索引')
# plt.show()


data2.fillna(0, inplace=True) #空值填充
data2['update_time'] = pd.to_datetime(data2['update_time']).apply(lambda x: x.strftime("%Y-%m-%d")) # 日期格式化，便于统计
data2[data2['sale_count']>0].sort_values(by=['sale_count']).head() # 从数据来看，sale_count 是销售量


data2['sale_amount'] = data2['price'] * data2['sale_count']  # 增加一列销售额
data2[data2['sale_count'] > 0].sort_values(by=['sale_count'])

result_data2_1 = data2.groupby(data2['update_time']).agg({'sale_count': 'sum'}).to_dict()['sale_count']

c = (
    Line()
    .add_xaxis(list(result_data2_1.keys()))
    .add_yaxis("销售量", list(result_data2_1.values()))
    .set_series_opts(
        label_opts=opts.LabelOpts(is_show=False),
        markpoint_opts=opts.MarkPointOpts(
            data=[
                opts.MarkPointItem(type_="max", name="最大值"),
                opts.MarkPointItem(type_="min", name="最小值"),
                opts.MarkPointItem(type_="average", name="平均值"),
            ]
        ),
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="每日销售量走势"))
)
c.render('每日销售量走势.html')


