# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.linear_model import LinearRegression
# # 生成随机数据
# num = 50
# np.random.seed(0)
# x_data = np.random.uniform(0,10,num)
# y_data = 0.5 * x_data + 1 + np.random.normal(0, 1, num)
# x_data = x_data.reshape((-1, 1))
# # 将x调整为列向量
# data = np.column_stack([x_data, y_data])
# # 创建回归对象并进行拟合
# LR = LinearRegression()
# # 使用LinearRegression()构建了一个线性回归模型
# LR.fit(x_data, y_data)
# slope = LR.coef_ # 斜率
# intercept = LR.intercept_ # 截距
# x_array = np.linspace(0, 10, 101).reshape((-1, 1))
# # 预测
# predicted = LR.predict(x_array)
# data_ = np.column_stack([x_data, LR.predict(x_data)])
# fig, ax = plt.subplots()
# ax.scatter(x_data, y_data)
# ax.scatter(x_data, LR.predict(x_data),
# color = 'k', marker = 'x')
# ax.plot(x_array, predicted,
# color = 'r')
# ax.plot(([i for (i,j) in data_], [i for (i,j) in data]),
# ([j for (i,j) in data_], [j for (i,j) in data]),
# c=[0.6,0.6,0.6], alpha = 0.5)
# ax.set_xlabel('x')
# ax.set_ylabel('y')
# ax.set_aspect('equal', adjustable='box')
# ax.set_xlim(0, 10)
# ax.set_ylim(-2, 8)
# plt.show()
#
# # 二元线性回归
# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.linear_model import LinearRegression
# # 随机生成数据集
# np.random.seed(0)
# n_samples = 100
# X = np.random.randn(n_samples, 2)
# y = -3 * X[:, 0] + 2 * X[:, 1] + 1 + 0.5*np.random.randn(n_samples)
# # 创建线性回归模型并拟合数据
# LR = LinearRegression()
# y_predicted = LR.fit(X, y)
# slope = LR.coef_ # 斜率
# intercept = LR.intercept_ # 截距
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# # 绘制三维样本散点
# ax.scatter(X[:,0], X[:,1], y)
# # 生成回归平面的数据点
# x1_grid, x2_grid = np.meshgrid(np.linspace(-3, 3, 10),
# np.linspace(-3, 3, 10))
# X_grid=np.column_stack((x1_grid.flatten(),x2_grid.flatten()))
# # 预测回归平面上的响应变量
# y_pred = LR.predict(X_grid)
# y_pred = y_pred.reshape(x1_grid.shape)
# # 绘制回归平面
# ax.plot_wireframe(x1_grid, x2_grid, y_pred)
# ax.set_xlabel('$x_1$'); ax.set_ylabel('$x_2$')
# ax.set_zlabel('y')
# ax.set_xlim([-3,3]); ax.set_ylim([-3,3])
# ax.set_proj_type('ortho'); ax.view_init(azim=-120, elev=30)
# plt.show()

# 多元线性回归
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
# 生成随机数据
np.random.seed(0)
num = 30
X = np.random.uniform(0,4,num)
y = np.sin(0.4*np.pi * X) + 0.4 * np.random.randn(num)
data = np.column_stack([X,y])
x_array = np.linspace(0,4,101).reshape(-1,1)
degree_array = [1,2,3,4,7,8]
fig, axes = plt.subplots(3,2,figsize=(10,20))
axes = axes.flatten()
for ax, degree_idx in zip(axes, degree_array):

    poly = PolynomialFeatures(degree=degree_idx)
    X_poly = poly.fit_transform(X.reshape(-1, 1))

    # 训练线性回归模型
    poly_reg = LinearRegression()
    poly_reg.fit(X_poly, y)
    y_poly_pred = poly_reg.predict(X_poly)
    data_ = np.column_stack([X, y_poly_pred])

    y_array_pred = poly_reg.predict(
        poly.fit_transform(x_array))

    # 绘制散点图
    ax.scatter(X, y, s=20)
    ax.scatter(X, y_poly_pred, marker='x', color='k')

    ax.plot(([i for (i, j) in data_], [i for (i, j) in data]),
            ([j for (i, j) in data_], [j for (i, j) in data]),
            c=[0.6, 0.6, 0.6], alpha=0.5)

    ax.plot(x_array, y_array_pred, color='r')
    ax.set_title('Degree = %d' % degree_idx)

    # 提取参数
    coef = poly_reg.coef_
    intercept = poly_reg.intercept_
    # 回归解析式
    equation = '$y = {:.1f}'.format(intercept)
    for j in range(1, len(coef)):
        equation += ' + {:.1f}x^{}'.format(coef[j], j)
    equation += '$'
    equation = equation.replace("+ -", "-")
    ax.text(0.05, -1.8, equation)
    ax.set_aspect('equal', adjustable='box')
    ax.set_xlim(0, 4)
    ax.grid(False)
    ax.set_ylim(-2, 2)
plt.show()

# 多项式回归

# 导入包
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import Ridge

# 生成随机数据
np.random.seed(0)
num = 30

X = np.random.uniform(0,4,num)
y = np.sin(0.4*np.pi * X) + 0.4 * np.random.randn(num)
data = np.column_stack([X,y])

x_array = np.linspace(0,4,101).reshape(-1,1)
degree = 8 # 多项式回归次数
# 将数据扩展为9列
poly = PolynomialFeatures(degree = degree)
X_poly = poly.fit_transform(X.reshape(-1, 1))

fig, axes = plt.subplots(3, 2, figsize=(10, 20))
axes = axes.flatten()
# 惩罚因子
alpha_array = [0.00001, 0.0001, 0.01, 1, 10, 100]

for ax, alpha_idx in zip(axes, alpha_array):

    # 训练岭回归模型
    ridge = Ridge(alpha=alpha_idx)
    ridge.fit(X_poly, y.reshape(-1, 1))
    # 预测
    y_array_pred = ridge.predict(poly.fit_transform(x_array))
    y_poly_pred = ridge.predict(X_poly)
    data_ = np.column_stack([X, y_poly_pred])
    # 绘制散点图
    ax.scatter(X, y, s=20)
    ax.scatter(X, y_poly_pred, marker='x', color='k')
    # 绘制残差
    ax.plot(([i for (i, j) in data_], [i for (i, j) in data]),
            ([j for (i, j) in data_], [j for (i, j) in data]),
            c=[0.6, 0.6, 0.6], alpha=0.5)

    ax.plot(x_array, y_array_pred, color='r')
    ax.set_title('Alpha = %f' % alpha_idx)

    # 提取参数
    coef = ridge.coef_[0];  # print(coef)
    intercept = ridge.intercept_[0];  # print(intercept)
    # 回归解析式
    equation = '$y = {:.3f}'.format(intercept)
    for j in range(1, len(coef)):
        equation += ' + {:.3f}x^{}'.format(coef[j], j)
    equation += '$'
    equation = equation.replace("+ -", "-")
    print(equation)
    ax.set_aspect('equal', adjustable='box')
    ax.set_xlim(0, 4)
    ax.set_ylim(-2, 2)
    ax.grid(False)
plt.show()


