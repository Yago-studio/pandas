# from sympy import symbols, factor
# # 从sympy中导入symbols, factor
# from sympy import init_printing
# init_printing("mathjax")
# x, y = symbols('x y')
# # 用sympy.symbols (简做symbols) 定义x和y两个符号变量
# f = x**2 - y**2
# f_factored = factor(f)
# print(f_factored)
#
# from sympy import symbols, sympify
# x, y = symbols('x y')
# str_expression = 'x**3 + x**2 + x + 1'
# # 将字符串转化为符号表达式
# str_2_sym = sympify(str_expression)
# # 将符号x替换为y
# str_2_sym.subs(x, y)
# # 将符号x替换为0
# str_2_sym.subs(x, 0)
#
#
# #求解等式
# from sympy import symbols,solve,Eq
# x = symbols('x')
# # 定义等式 x**2 = 1
# equation_1 = Eq(x**2, 1)
# solve(equation_1, x)
# a,b,c = symbols("a,b,c", real=True)
# # 定义等式 a*x**2+b*x = -c
# equation_2 = Eq(a*x**2+b*x+c, 0)
# print(solve(equation_2, x))
#
#
# from sympy import symbols, exp, lambdify
# import numpy as np
# import matplotlib.pyplot as plt
# x1, x2 = symbols('x1 x2')
# # 定义符号变量
# f_gaussian_x1x2 = exp(-x1**2 - x2**2)
# # 将符号表达式转换为Python函数
# f_gaussian_x1x2_fcn = lambdify([x1,x2],f_gaussian_x1x2)
# xx1,xx2 = np.meshgrid(np.linspace(-3,3,201),
# np.linspace(-3,3,201))
# ff = f_gaussian_x1x2_fcn(xx1, xx2)
# # 可视化
# fig = plt.figure()
# ax = fig.add_subplot(projection='3d')
# ax.plot_wireframe(xx1,xx2,ff,
# rstride=10, cstride=10)
# ax.set_proj_type('ortho')
# ax.view_init(azim=-120, elev=30)
# ax.grid(False)
# ax.set_xlabel('x1')
# ax.set_ylabel('x2')
# ax.set_zlabel('f(x1,x2)')
# ax.set_xlim(-3, 3)
# ax.set_ylim(-3, 3)
# ax.set_zlim(0, 1)
# ax.set_box_aspect(aspect=(1, 1, 1))
# # fig.savefig('二元高斯函数.png', format='png')
# plt.show()
#
# #线性代数
# from sympy import Matrix
# # 定义矩阵
# A = Matrix([[1, 2, 3], [3, 2, 1]])
# # 定义列向量
# a = Matrix([1, 2, 3])
#
# from sympy import symbols
# A = Matrix([[1, 3], [-2, 3]])
# B = Matrix([[0, 3], [0, 7]])
# A.T # 矩阵转置
# A + B # 加法
# A - B # 减法
# 3*A # 标量乘矩阵
# A.multiply_elementwise(B) # 逐项积
# A * B # 矩阵乘法
# A @ B # 矩阵乘法
# Matrix_2x2 = Matrix([[1.25, -0.75],
# [-0.75, 1.25]])
# Matrix_2x2**-1 # 矩阵逆
# Matrix_2x2.inv() # 矩阵逆
# # 将符号矩阵转化为浮点数numpy数组
# np.array(Matrix_2x2).astype(np.float64)
# a, b, c, d = symbols('a b c d')
# Q = Matrix([[a, b],
# [c, d]])
# Q.inv() # 矩阵逆
# Q.det() # 行列式
# Q.trace() # 迹


# 正定性
# 导入包
import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols, lambdify, expand, simplify
# 定义可视化函数
def visualize(xx1,xx2,f2_array, name):
    fig = plt.figure(figsize=(6,3))
# 左子图，三维
    ax_3D = fig.add_subplot(1, 2, 1, projection='3d')
    ax_3D.plot_wireframe(xx1, xx2, f2_array,
    rstride=10, cstride=10,
    color = [0.8,0.8,0.8],
    linewidth = 0.25)
    ax_3D.contour(xx1, xx2, f2_array,
    levels = 12, cmap = 'RdYlBu_r')
    ax_3D.set_xlabel('$x_1$'); ax_3D.set_ylabel('$x_2$')
    ax_3D.set_zlabel('$f(x_1,x_2)$')
    ax_3D.set_proj_type('ortho')
    ax_3D.set_xticks([]); ax_3D.set_yticks([])
    ax_3D.set_zticks([])
    ax_3D.view_init(azim=-120, elev=30)
    ax_3D.grid(False)
    ax_3D.set_xlim(xx1.min(), xx1.max());
    ax_3D.set_ylim(xx2.min(), xx2.max())
# 右子图，平面等高线
    ax_2D = fig.add_subplot(1, 2, 2)
    ax_2D.contour(xx1, xx2, f2_array,
    levels = 12, cmap = 'RdYlBu_r')
    ax_2D.set_xlabel('$x_1$'); ax_2D.set_ylabel('$x_2$')
    ax_2D.set_xticks([]); ax_2D.set_yticks([])
    ax_2D.set_aspect('equal'); ax_2D.grid(False)
    ax_2D.set_xlim(xx1.min(), xx1.max());
    ax_2D.set_ylim(xx2.min(), xx2.max())
    plt.tight_layout()
    plt.show()
    # fig.savefig(f'{name}.png', format='png')


# 生成数据
x1_array = np.linspace(-2,2,201)
x2_array = np.linspace(-2,2,201)
xx1, xx2 = np.meshgrid(x1_array, x2_array)
# 定义二元函数
def fcn(A, xx1, xx2):
     x1,x2 = symbols('x1 x2')
     x = np.array([[x1,x2]]).T
     f_x = x.T@A@x
     f_x = f_x[0][0]
     print(simplify(expand(f_x)))
     f_x_fcn = lambdify([x1,x2],f_x)
     ff_x = f_x_fcn(xx1,xx2)
     return ff_x
# 不定矩阵
A = np.array([[0, 1],
[1, 0]])
f2_array = fcn(A, xx1, xx2)
visualize(xx1,xx2,f2_array, name='bea')
