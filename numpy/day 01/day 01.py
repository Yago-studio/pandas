from sklearn.datasets import load_iris

iris = load_iris()

X = iris.data

type(X)

y = iris.target

type(y)

import seaborn as sns

iris_df = sns.load_dataset("iris")

print(iris_df.head())

type(iris_df)

