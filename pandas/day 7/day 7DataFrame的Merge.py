import pandas as pd


df_ratings = pd.read_csv(
    "E:\数据集\ml-1m/ratings.dat",
    encoding="latin1",
    sep="::",
    engine='python',
    names="UserID::MovieID::Rating::Timestamp".split("::"),
)

df_users = pd.read_csv(
    "E:\数据集\ml-1m/users.dat",
    encoding="latin1",
    sep="::",
    engine='python',
    names="UserID::Gender::Age::Occupation::Zip-code".split("::")
)

df_movies = pd.read_csv(
    "E:\数据集\ml-1m/movies.dat",
    encoding="latin1",
    sep="::",
    engine='python',
    names="MovieID::Title::Genres".split("::")
)

df_ratings_users = pd.merge(
   df_ratings, df_users, left_on="UserID", right_on="UserID", how="inner"
)
# print(df_ratings_users.head())


df_ratings_users_movies = pd.merge(
    df_ratings_users, df_movies, left_on="MovieID", right_on="MovieID", how="inner"
)


print(df_ratings_users_movies.head())

# 2.merge时数量的对齐关系
# 2.1 one-to-one 一对一关系的merge

left = pd.DataFrame({'sno': [11, 12, 13, 14],
                      'name': ['name_a', 'name_b', 'name_c', 'name_d']
                    })
right = pd.DataFrame({'sno': [11, 12, 13, 14],
                      'age': ['21', '22', '23', '24']
                    })


print(pd.merge(left, right, on='sno'))

# 2.2 one-to-many 一对多关系的merge
left = pd.DataFrame({'sno': [11, 12, 13, 14],
                      'name': ['name_a', 'name_b', 'name_c', 'name_d']
                    })

right = pd.DataFrame({'sno': [11, 11, 11, 12, 12, 13],
                       'grade': ['语文88', '数学90', '英语75', '语文66', '数学55', '英语29']
                     })

# 2.3 many-to-many 多对多关系的merge

left = pd.DataFrame({'sno': [11, 11, 12, 12,12],
                      '爱好': ['篮球', '羽毛球', '乒乓球', '篮球', "足球"]
                    })

right = pd.DataFrame({'sno': [11, 11, 11, 12, 12, 13],
                       'grade': ['语文88', '数学90', '英语75', '语文66', '数学55', '英语29']
                     })

# 3、理解left join、right join、inner join、outer join的区别

left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                      'A': ['A0', 'A1', 'A2', 'A3'],
                      'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key': ['K0', 'K1', 'K4', 'K5'],
                      'C': ['C0', 'C1', 'C4', 'C5'],
                      'D': ['D0', 'D1', 'D4', 'D5']})

pd.merge(left, right, how='inner')

pd.merge(left, right, how='left')

pd.merge(left, right, how='right')

# 4、如果出现非Key的字段重名怎么办
left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                      'A': ['A0', 'A1', 'A2', 'A3'],
                      'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key': ['K0', 'K1', 'K4', 'K5'],
                      'A': ['A10', 'A11', 'A12', 'A13'],
                      'D': ['D0', 'D1', 'D4', 'D5']})

pd.merge(left, right, on='key')

pd.merge(left, right, on='key', suffixes=('_left', '_right'))

