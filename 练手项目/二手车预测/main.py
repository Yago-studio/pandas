import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# 设置 Matplotlib 使用支持中文的字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

import re

from scipy.stats import chi2_contingency, ks_2samp, spearmanr, f_oneway
from datetime import datetime
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import RidgeCV, Ridge
from sklearn.preprocessing import StandardScaler

train_data = pd.read_csv("E:\数据集\二手车价格预测数据集/train.csv", encoding='utf-8')
test_data = pd.read_csv("E:\数据集\二手车价格预测数据集/test.csv", encoding='utf-8')

# 查看重复值
print(f'训练集中存在的重复值：{train_data.duplicated().sum()}')
print(f'测试集中存在的重复值：{test_data.duplicated().sum()}')


# 查看分类特征的唯一值
characteristic = train_data.select_dtypes(include=['object']).columns
# print('训练集中分类变量的唯一值情况：')
# for i in characteristic:
#     print(f'{i}:')
#     print(f'共有:{len(train_data[i].unique())}条唯一值')
#     print(train_data[i].unique())
#     print('-'*50)

plt.figure(figsize=(10, 6))

sns.heatmap(train_data.isna(), cbar=False, cmap='viridis', yticklabels=False)
plt.title('训练集缺失值热图')
plt.xlabel('字段名')
plt.ylabel('样本索引')

plt.figure(figsize=(10,6))
sns.heatmap(test_data.isna(), cbar=False, cmap='viridis', yticklabels=False)
plt.title('测试集缺失值热图')
plt.xlabel('字段名')
plt.ylabel('样本索引')
plt.show()

# 处理燃料类型缺失值：按品牌和型号填充，若无法确定则使用品牌的众数
# 首先将 '–' 标记为缺失值
train_data['fuel_type'] = train_data['fuel_type'].replace('–', np.nan)
test_data['fuel_type'] = test_data['fuel_type'].replace('–', np.nan)
# 处理燃料类型缺失值：按品牌和型号填充，若无法确定则使用品牌的众数
fuel_type_mode_by_brand_model = train_data.groupby(['brand', 'model'])['fuel_type'].apply(lambda x: x.mode().iloc[0] if not x.mode().empty else None)
fuel_type_mode_by_brand = train_data.groupby('brand')['fuel_type'].apply(lambda x: x.mode().iloc[0] if not x.mode().empty else None)

def fill_fuel_type(row):
    if pd.isnull(row['fuel_type']):
        # 先按品牌和型号填充
        brand_model_fill = fuel_type_mode_by_brand_model.get((row['brand'], row['model']), None)
        # 若品牌和型号均缺失，按品牌填充
        return brand_model_fill if brand_model_fill is not None else fuel_type_mode_by_brand.get(row['brand'], 'Gasoline')
    return row['fuel_type']

# 应用填充方法到训练集和测试集
train_data['fuel_type'] = train_data.apply(fill_fuel_type, axis=1)
test_data['fuel_type'] = test_data.apply(fill_fuel_type, axis=1)

# 处理事故历史缺失值：删除有缺失值的行
train_data.dropna(subset=['accident'], inplace=True)
test_data.dropna(subset=['accident'], inplace=True)

# 删除训练集和测试集中的 clean_title 列
train_data.drop(columns=['clean_title'], inplace=True)
test_data.drop(columns=['clean_title'], inplace=True)

# 检查缺失值情况
train_missing = train_data.isnull().sum()
test_missing = test_data.isnull().sum()
print('处理后的训练集缺失值情况:')
print(train_missing)
print('-'*50)
print('处理后的测试集缺失值情况:')
print(test_missing)

# 定义函数，用于提取符合 "X.XL" 格式的排量信息
def extract_displacement(engine_info):
    match = re.search(r'(\d+\.\d+)L', str(engine_info))  # 匹配标准格式的排量
    if match:
        return float(match.group(1))  # 提取数值部分并转化为浮点数
    return None  # 若没有匹配到排量信息，则返回 None

# 应用函数提取排量信息，生成新的 'displacement' 列
train_data['displacement'] = train_data['engine'].apply(extract_displacement)
test_data['displacement'] = test_data['engine'].apply(extract_displacement)

# 统计训练集和测试集中 'displacement' 列的缺失值数量
train_displacement_missing_count = train_data['displacement'].isnull().sum()
test_displacement_missing_count = test_data['displacement'].isnull().sum()
print(f'训练集中不符合正则提取规则的数据数量:{train_displacement_missing_count}')
print(f'测试集中不符合正则提取规则的数据数量:{test_displacement_missing_count}')

# 查看训练集中缺失排量信息的前10条数据
train_missing_displacement_samples = train_data[train_data['displacement'].isnull()][['engine']].head(10)
train_missing_displacement_samples


# 更新提取函数：先提取排量信息，若没有排量则判断是否为电动
def extract_displacement_corrected(engine_info):
    engine_str = str(engine_info).lower()
    # 优先提取排量信息
    displacement_match = re.search(r'(\d+\.\d+)\s?(l|liter)', engine_str)
    if displacement_match:
        return float(displacement_match.group(1))  # 提取排量数值
    # 若未提取到排量，再判断是否为电动
    if "electric" in engine_str:
        return "Electric"
    return None  # 无法匹配的返回 None


# 应用更新后的提取函数
train_data['displacement'] = train_data['engine'].apply(extract_displacement_corrected)
test_data['displacement'] = test_data['engine'].apply(extract_displacement_corrected)

# 再次统计缺失值数量，以确认处理效果
train_displacement_missing_updated = train_data['displacement'].isnull().sum()
test_displacement_missing_updated = test_data['displacement'].isnull().sum()
print(f'训练集中不符合正则提取规则的数据数量:{train_displacement_missing_updated}')
print(f'测试集中不符合正则提取规则的数据数量:{test_displacement_missing_updated}')

# 输出训练集中缺失排量信息的前10条数据，便于进一步分析
train_missing_displacement_final_samples = train_data[train_data['displacement'].isnull()][['engine']].head(10)
train_missing_displacement_final_samples

# 1. 处理训练集中短描述和无效标记的情况
# 定义缺失值的短描述和无效标记的列表
short_descriptions = ['v6', 'v8', 'i4', 'i6', 'v12']
invalid_marks = ['–']
# 预计算各品牌的排量中位数和每种类型的众数排量
# 计算每个品牌的排量中位数（排除 'Electric' 标记）
brand_median_displacement = train_data[train_data['displacement'] != "Electric"].groupby('brand')[
    'displacement'].median()

# 计算每种短描述（类型）的众数排量
type_mode_displacement = {}
for short_desc in short_descriptions + invalid_marks:
    mode_value = train_data[train_data['engine'].str.contains(short_desc, case=False, na=False)]['displacement'].mode()
    type_mode_displacement[short_desc] = mode_value.iloc[0] if not mode_value.empty else None


# 更新填充函数，直接引用预计算的中位数和众数值
def fill_displacement_optimized(row):
    if pd.notnull(row['displacement']):
        return row['displacement']

    engine_str = str(row['engine']).lower()

    # 尝试按类型众数填充
    for short_desc in short_descriptions + invalid_marks:
        if short_desc in engine_str:
            if type_mode_displacement[short_desc] is not None:
                return type_mode_displacement[short_desc]

    # 按品牌中位数填充
    if row['brand'] in brand_median_displacement:
        return brand_median_displacement[row['brand']]

    # 标记电动
    if 'dual motor' in engine_str or 'battery' in engine_str or 'electric' in engine_str:
        return "Electric"

    return np.nan


# 应用填充函数到训练集和测试集
train_data['displacement'] = train_data.apply(fill_displacement_optimized, axis=1)
test_data['displacement'] = test_data.apply(fill_displacement_optimized, axis=1)
# 再次统计缺失值数量，以确认处理效果
train_displacement_missing_final_optimized = train_data['displacement'].isnull().sum()
test_displacement_missing_final_optimized = test_data['displacement'].isnull().sum()
print(f'训练集中不符合正则提取规则的数据数量:{train_displacement_missing_final_optimized}')
print(f'测试集中不符合正则提取规则的数据数量:{test_displacement_missing_final_optimized}')

# 定义函数，根据排量划分等级
def categorize_displacement(displacement):
    # 对电动车直接返回 Electric
    if displacement == "Electric":
        return "Electric"
    # 判断数值的区间，并返回相应的类别
    elif displacement <= 1.0:
        return "Small"
    elif 1.0 < displacement <= 1.6:
        return "Medium"
    elif 1.6 < displacement <= 2.5:
        return "Large"
    elif 2.5 < displacement <= 4.0:
        return "Extra-large"
    else:
        return "Ultra-large"

# 应用划分函数到训练集和测试集
train_data['displacement'] = train_data['displacement'].apply(categorize_displacement)
test_data['displacement'] = test_data['displacement'].apply(categorize_displacement)

# 删除训练集和测试集中的 engine 列
train_data.drop(columns=['engine'], inplace=True)
test_data.drop(columns=['engine'], inplace=True)


# 定义函数，将变速器类型分为 'Automatic'、'Manual' 和 'Other'
def categorize_transmission(transmission):
    transmission = str(transmission).lower()
    if any(keyword in transmission for keyword in ["automatic", "a/t", "cvt", "speed"]):
        return "Automatic"
    elif any(keyword in transmission for keyword in ["manual", "m/t"]):
        return "Manual"
    else:
        return "Other"

# 应用函数到训练集和测试集
train_data['transmission'] = train_data['transmission'].apply(categorize_transmission)
test_data['transmission'] = test_data['transmission'].apply(categorize_transmission)

# 定义函数，将变速器类型分为 'Automatic'、'Manual' 和 'Other'
def categorize_transmission(transmission):
    transmission = str(transmission).lower()
    if any(keyword in transmission for keyword in ["automatic", "a/t", "cvt", "speed"]):
        return "Automatic"
    elif any(keyword in transmission for keyword in ["manual", "m/t"]):
        return "Manual"
    else:
        return "Other"

# 应用函数到训练集和测试集
train_data['transmission'] = train_data['transmission'].apply(categorize_transmission)
test_data['transmission'] = test_data['transmission'].apply(categorize_transmission)


# 定义函数，将外饰颜色分类
def categorize_exterior_color(color):
    color = str(color).lower()  # 转为小写方便匹配
    if "silver" in color or "gray" in color or "grey" in color:
        return "Silver gray"
    elif "white" in color:
        return "White"
    elif "black" in color:
        return "Black"
    elif "red" in color:
        return "Red"
    elif "blue" in color:
        return "Blue"
    elif "yellow" in color:
        return "Yellow"
    elif "green" in color:
        return "Green"
    else:
        return "Other"

# 应用分类函数到训练集和测试集的外饰颜色列
train_data['ext_col'] = train_data['ext_col'].apply(categorize_exterior_color)
test_data['ext_col'] = test_data['ext_col'].apply(categorize_exterior_color)


# 定义函数，将内饰颜色分类
def categorize_interior_color(color):
    color = str(color).lower()  # 转为小写方便匹配
    if "black" in color:
        return "Black"
    elif "white" in color:
        return "White"
    elif "brown" in color:
        return "Brown"
    elif "red" in color:
        return "Red"
    elif "beige" in color:
        return "Beige"
    else:
        return "Other"

# 应用分类函数到训练集和测试集的内饰颜色列
train_data['int_col'] = train_data['int_col'].apply(categorize_interior_color)
test_data['int_col'] = test_data['int_col'].apply(categorize_interior_color)

# 检查数据集中每列的缺失值数量
print("训练集缺失值统计：")
print(train_data.isnull().sum())

print("\n测试集缺失值统计：")
print(test_data.isnull().sum())

# 检查是否还存在包含 "–" 的情况
def check_dash_values(df):
    dash_counts = {}
    for col in df.columns:
        dash_counts[col] = df[col].astype(str).str.contains("–").sum()
    return pd.Series(dash_counts, name="Dash Count")

print("\n训练集中包含 '–' 的情况：")
print(check_dash_values(train_data))

print("\n测试集中包含 '–' 的情况：")
print(check_dash_values(test_data))


train_data['log_price'] = np.log1p(train_data['price'])  # log1p避免log(0)的问题



# 添加一个列来区分训练集和测试集
train_data['dataset'] = 'train'
test_data['dataset'] = 'test'
# 合并数据
combined_df = pd.concat([train_data, test_data], ignore_index=True)
plt.figure(figsize=(20,15))
plt.subplot(2,4,1)
sns.kdeplot(data=combined_df, x='model_year', hue='dataset', common_norm=False)
plt.title(f'汽车的制造年份在训练集和测试集核密度分布图')
plt.xlabel('汽车的制造年份')
plt.ylabel('密度')
plt.legend(title='数据集', labels=['train', 'test'])

plt.subplot(2,4,2)
sns.kdeplot(data=combined_df, x='milage', hue='dataset', common_norm=False)
plt.title(f'汽车的行驶里程在训练集和测试集核密度分布图')
plt.xlabel('汽车的行驶里程')
plt.ylabel('密度')
plt.legend(title='数据集', labels=['train', 'test'])

plt.subplot(2,4,3)
fuel_type_counts = combined_df.groupby(['dataset', 'fuel_type']).size().unstack()
fuel_type_proportions = fuel_type_counts.div(fuel_type_counts.sum(axis=1), axis=0)
fuel_type_proportions.plot(kind='bar', stacked=True, ax=plt.gca())
plt.title(f'汽车所使用的燃料类型在训练集和测试集中占比分布')
plt.xlabel('数据集')
plt.xticks(rotation=0)
plt.legend(loc='upper right')
plt.ylabel('占比')

plt.subplot(2,4,4)
transmission_counts = combined_df.groupby(['dataset', 'transmission']).size().unstack()
transmission_proportions = transmission_counts.div(transmission_counts.sum(axis=1), axis=0)
transmission_proportions.plot(kind='bar', stacked=True, ax=plt.gca())
plt.title(f'变速器类型在训练集和测试集中占比分布')
plt.xlabel('数据集')
plt.xticks(rotation=0)
plt.legend(loc='upper right')
plt.ylabel('占比')

plt.subplot(2,4,5)
ext_col_counts = combined_df.groupby(['dataset', 'ext_col']).size().unstack()
ext_col_proportions = ext_col_counts.div(ext_col_counts.sum(axis=1), axis=0)
ext_col_proportions.plot(kind='bar', stacked=True, ax=plt.gca())
plt.title(f'外观颜色在训练集和测试集中占比分布')
plt.xlabel('数据集')
plt.xticks(rotation=0)
plt.legend(loc='upper right')
plt.ylabel('占比')

plt.subplot(2,4,6)
int_col_counts = combined_df.groupby(['dataset', 'int_col']).size().unstack()
int_col_proportions = int_col_counts.div(int_col_counts.sum(axis=1), axis=0)
int_col_proportions.plot(kind='bar', stacked=True, ax=plt.gca())
plt.title(f'内饰颜色在训练集和测试集中占比分布')
plt.xlabel('数据集')
plt.xticks(rotation=0)
plt.legend(loc='upper right')
plt.ylabel('占比')

plt.subplot(2,4,7)
accident_counts = combined_df.groupby(['dataset', 'accident']).size().unstack()
accident_proportions = accident_counts.div(accident_counts.sum(axis=1), axis=0)
accident_proportions.plot(kind='bar', stacked=True, ax=plt.gca())
plt.title(f'车辆有事故或损坏的历史记录在训练集和测试集中占比分布')
plt.xlabel('数据集')
plt.xticks(rotation=0)
plt.legend(loc='upper right')
plt.ylabel('占比')

plt.subplot(2,4,8)
displacement_counts = combined_df.groupby(['dataset', 'displacement']).size().unstack()
displacement_proportions = displacement_counts.div(displacement_counts.sum(axis=1), axis=0)
displacement_proportions.plot(kind='bar', stacked=True, ax=plt.gca())
plt.title(f'排量大小在训练集和测试集中占比分布')
plt.xlabel('数据集')
plt.xticks(rotation=0)
plt.legend(loc='upper right')
plt.ylabel('占比')

plt.tight_layout()
plt.show()


# 删除训练集和测试集中的 dataset 列
train_data.drop(columns=['dataset'], inplace=True)
test_data.drop(columns=['dataset'], inplace=True)

results = []
categorical_features = train_data.select_dtypes(include=['object']).columns
for feature in categorical_features:
    table = pd.crosstab(train_data[feature], test_data[feature])
    chi2, p, dof, expected = chi2_contingency(table)
    results.append({'Feature': feature, 'Statistic': chi2, 'p-value': p})
results_df = pd.DataFrame(results)



numerical_features = ['model_year','milage']
results = []
for feature in numerical_features:
    statistic, p_value = ks_2samp(train_data[feature], test_data[feature])
    results.append({'Feature': feature,'Statistic': statistic, 'p-value': p_value})
results_df = pd.DataFrame(results)





