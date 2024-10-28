# import pandas as pd
# import plotly.express as px
# import re
#
#
# # 定义数据处理和可视化函数
# def analyze_salary(
#         path,
#         job_keywords=None,
#         skill_keywords=None,
#         degree_keywords=None,
#         experience_keywords=None
# ):
#     # 读取数据
#     df = pd.read_csv(path)
#
#     # 删除包含空值的列
#     df.dropna(how='any', axis=1, inplace=True)
#
#     # 修改列名称为中文
#     df.columns = ['公司', '职位', '工作地点', '薪资待遇', '教育经历', '个人经历', '岗位要求', "具体描述"]
#
#     # 筛选包含任意 job_keywords 中关键词的数据
#     if job_keywords:
#         task1 = df[df['职位'].apply(lambda x: any(keyword in str(x) for keyword in job_keywords))]
#     else:
#         task1 = df
#
#     # 筛选岗位要求中包含 skill_keywords 中任意关键词的数据
#     if skill_keywords:
#         task2 = task1[task1['岗位要求'].apply(lambda x: any(keyword in str(x) for keyword in skill_keywords))]
#     else:
#         task2 = task1
#
#     # 筛选教育经历包含 degree_keywords 中任意关键词的数据
#     if degree_keywords:
#         task3 = task2[task2['教育经历'].apply(lambda x: any(keyword in str(x) for keyword in degree_keywords))]
#     else:
#         task3 = task2
#
#     # 筛选个人经历包含 experience_keywords 中任意关键词的数据
#     if experience_keywords:
#         task4 = task3[task3['个人经历'].apply(lambda x: any(keyword in str(x) for keyword in experience_keywords))]
#     else:
#         task4 = task3
#
#     # 重置索引
#     task4.reset_index(drop=True, inplace=True)
#
#     # 定义年薪计算函数
#     def salary_year(s):
#         pattern = r'\d+'
#         sal_num = re.findall(pattern, s)
#         sal_num = list(map(int, sal_num))
#
#         # 根据不同薪酬描述计算年薪
#         if '薪' in s:
#             return (sal_num[0] + sal_num[1] / 2) * sal_num[2] if len(sal_num) >= 3 else sal_num[0]
#         elif '天' in s:
#             return (sal_num[0] + sal_num[1] / 2) * 205 * 0.001 if len(sal_num) >= 2 else sal_num[0] * 205 * 0.001
#         elif '月' in s:
#             return (sal_num[0] + sal_num[1] / 2) * 12 * 0.001 if len(sal_num) >= 2 else sal_num[0] * 12 * 0.001
#         else:
#             return (sal_num[0] + sal_num[1] / 2) * 12 if len(sal_num) >= 2 else sal_num[0] * 12
#
#     # 计算年薪并将单位调整为万元
#     task4['年薪(w)'] = task4['薪资待遇'].apply(salary_year) / 10
#
#     # 按工作地点分组计算平均年薪，并按降序排序
#     y = task4.groupby('工作地点').agg({'年薪(w)': 'mean'}).sort_values(by='年薪(w)', ascending=False)['年薪(w)']
#     x = y.index  # 工作地点作为 x 轴数据
#
#     # 绘制条形图
#     fig = px.bar(x=x, y=y.values, labels={'x': '工作地点', 'y': '平均年薪（w）'}, title='不同工作地点的平均年薪')
#     fig.show()
#
#     # 保存数据至 CSV 文件（可选）
#     task4.to_csv('jobs_search.csv', index=False)
#
#
# # 调用函数，传入文件路径和关键词列表
# path = "D:\pythonTest\量化分析\数据集\招聘网站岗位信息\jobs.csv"
# analyze_salary(
#     path,
#     job_keywords=['后端'],
#     skill_keywords=[],
#     degree_keywords=['本科', '专科'],
#     experience_keywords=['经验不限', '1-3年']
# )


import pandas as pd
import re
import plotly.express as px
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt


# 1. 数据预处理
def preprocess_data(path):
    # 加载数据
    df = pd.read_csv(path)
    df.dropna(how='any', axis=1, inplace=True)
    df.columns = ['公司', '职位', '工作地点', '薪资待遇', '教育经历', '个人经历', '岗位要求', "具体描述"]


    # 薪资数据转换年薪
    def salary_year(s):
        pattern = r'\d+'
        sal_num = re.findall(pattern, s)
        sal_num = list(map(int, sal_num))
        if '薪' in s:
            return (sal_num[0] + sal_num[1] / 2) * sal_num[2] if len(sal_num) >= 3 else sal_num[0]
        elif '天' in s:
            return (sal_num[0] + sal_num[1] / 2) * 205 * 0.001 if len(sal_num) >= 2 else sal_num[0] * 205 * 0.001
        elif '月' in s:
            return (sal_num[0] + sal_num[1] / 2) * 12 * 0.001 if len(sal_num) >= 2 else sal_num[0] * 12 * 0.001
        else:
            return (sal_num[0] + sal_num[1] / 2) * 12 if len(sal_num) >= 2 else sal_num[0] * 12

    df['年薪(w)'] = df['薪资待遇'].apply(salary_year) / 10
    return df


# 2. 薪资分析
def salary_analysis(df):
    # 年薪分布
    fig = px.histogram(df, x='年薪(w)', nbins=30, title='年薪分布')
    fig.show()

    # 行业或岗位的平均薪资
    position_salary = df.groupby('职位')['年薪(w)'].mean().sort_values(ascending=False)
    fig = px.bar(position_salary, x=position_salary.index, y=position_salary.values, title="不同职位的平均年薪")
    fig.show()

    # 薪资与经验的关系
    experience_salary = df.groupby('个人经历')['年薪(w)'].mean()
    fig = px.line(experience_salary, x=experience_salary.index, y=experience_salary.values,
                  title="薪资与工作经验的关系")
    fig.show()


# 3. 地域分布
def location_distribution(df):
    # 职位发布的地域分布
    location_count = df['工作地点'].value_counts()
    fig = px.bar(location_count, x=location_count.index, y=location_count.values, title="职位发布的地域分布")
    fig.show()

    # 地域薪资差异
    location_salary = df.groupby('工作地点')['年薪(w)'].mean().sort_values(ascending=False)
    fig = px.bar(location_salary, x=location_salary.index, y=location_salary.values, title="不同工作地点的平均年薪")
    fig.show()


# 4. 职位要求分析
def job_requirements_analysis(df):
    # 技能词频分析
    all_skills = ' '.join(df['岗位要求'].dropna())
    skill_counts = Counter(all_skills.split())
    skill_df = pd.DataFrame(skill_counts.items(), columns=['技能', '频次']).sort_values(by='频次', ascending=False)

    fig = px.bar(skill_df.head(10), x='技能', y='频次', title='最受欢迎的技能')
    fig.show()

    # 绘制词云
    wordcloud = WordCloud(width=800, height=400).generate(all_skills)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()

    # 学历要求分布
    degree_count = df['教育经历'].value_counts()
    fig = px.pie(degree_count, names=degree_count.index, values=degree_count.values, title="学历要求分布")
    fig.show()


# 5. 工作年限与学历的关系
def experience_degree_relationship(df):
    # 学历与经验
    experience_degree = df.groupby(['教育经历', '个人经历']).size().unstack()
    fig = px.imshow(experience_degree, title="学历与经验的关系", labels=dict(x="个人经历", y="教育经历"))
    fig.show()

    # 经验对职位的影响
    experience_job = df.groupby(['职位', '个人经历']).size().unstack()
    fig = px.imshow(experience_job, title="经验对职位的影响", labels=dict(x="个人经历", y="职位"))
    fig.show()


# 6. 热门职位和公司分析
def popular_jobs_companies(df):
    # 热门职位
    job_count = df['职位'].value_counts()
    fig = px.bar(job_count.head(10), x=job_count.index, y=job_count.values, title="热门职位")
    fig.show()

    # 公司薪资对比
    company_salary = df.groupby('公司')['年薪(w)'].mean().sort_values(ascending=False)
    fig = px.bar(company_salary.head(10), x=company_salary.index, y=company_salary.values, title="公司薪资对比")
    fig.show()


# 7. 主函数
def main():
    path = "D:\pythonTest\量化分析\数据集\招聘网站岗位信息\jobs.csv"  # 数据路径
    df = preprocess_data(path)

    salary_analysis(df)  # 薪资分析
    location_distribution(df)  # 地域分布
    job_requirements_analysis(df)  # 职位要求分析
    experience_degree_relationship(df)  # 工作年限与学历的关系
    popular_jobs_companies(df)  # 热门职位和公司分析




# 运行主函数
if __name__ == "__main__":
    main()


