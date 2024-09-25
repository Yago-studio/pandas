import pandas as pd

df = pd.read_csv("../test.csv")

# 1、Series的排序
#从小到大
print(df["total_amount"].sort_values())

df["total_amount"].sort_values(ascending=False)

# 2、DataFrame的排序
#（1）.单排排序
df.sort_values(by="total_amount")

#（2）.多列排序
print(df.sort_values(by=["total_amount", "insurance_agent_id"]))

df.sort_values(by=["total_amount", "insurance_agent_id"], ascending=[True, False])
