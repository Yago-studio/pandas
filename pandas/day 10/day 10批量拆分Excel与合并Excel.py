import pandas as pd

df_source = pd.read_csv(f"/test.csv")

total_row_count = df_source.shape[0]

# 一、将一个大Excel等份拆成多个Excel
# 这个大excel，会拆分给这几个人
user_names = ["xiao_shuai", "xiao_wang", "xiao_ming", "xiao_lei", "xiao_bo"]

# 每个人的任务数目
split_size = total_row_count // len(user_names)
if total_row_count % len(user_names) != 0:
    split_size += 1

df_subs = []
# for idx, user_name in enumerate(user_names):
#     # iloc的开始索引
#     begin = idx*split_size
#     # iloc的结束索引
#     end = begin+split_size
#     # 实现df按照iloc拆分
#     print(begin, end)
#     df_sub = df_source.iloc[begin:end]
#     print(df_sub.size)
#     # 将每个子df存入列表
#     df_subs.append((idx, user_name, df_sub))
#
# for idx, user_name, df_sub in df_subs:
#     file_name = f"crazyant_blog_articles_{idx}_{user_name}.xlsx"
#     df_sub.to_excel(file_name, index=False)


# 二、合并多个小Excel到一个大Excel
import os

origin_path = "/pandas/day 10/excel"
excel_names = []
for excel_name in os.listdir(origin_path):
    excel_names.append(excel_name)
# print(excel_names)

# 2.分别读取到dataframe
df_list = []


for excel_name in excel_names:
    # 读取每个excel到df
    excel_path = f"{origin_path}/{excel_name}"
    # print(excel_path)
    df_split = pd.read_excel(excel_path)
    # 得到username
    username = excel_name.replace("crazyant_blog_articles_", "").replace(".xlsx", "")[2:]
    print(excel_name, username)
    # 给每个df添加1列，即用户名字
    df_split["username"] = username

    df_list.append(df_split)

# 3.使用pd.concat进行合并
df_merged = pd.concat(df_list)

df_merged["username"].value_counts()

df_merged.to_excel(f"crazyant_blog_articles_merged.xlsx", index=False)


