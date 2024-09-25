import pandas as pd


studf = pd.read_csv("../test.csv", skiprows=0)

# 步骤2：检测空值

# print(studf.isnull())

# studf["renew_from_id"].isnull()

# studf["create_time"].notnull()

# 筛选renew_from_id不为空的所有行
studf.loc[studf["renew_from_id"].isnull(), :]


# 步骤3：删除掉全是空值的列
# studf.dropna(axis="columns", how='all', inplace=True)

#步骤4：删除掉全是空值的行

# studf.dropna(axis="index", how='all', inplace=True)

#步骤5：将分数列为空的填充为0分

# studf.fillna({"renew_from_id": 0})

# 如果数据中有空值未被删除，这个步骤会报keyerror的错，需要跳过3，4步骤
studf.loc[:, 'renew_from_id'] = studf['renew_from_id'].fillna(0)

#步骤6：将姓名的缺失值填充
#默认填充上个最近的值
# studf.loc[:, '姓名'] = studf['姓名'].fillna(method="ffill")

#步骤7：将清洗好的excel保存

studf.to_excel("test_excel_clean.xlsx", index=False)

