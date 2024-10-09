import numpy as np

# 自定义函数
# def matrix_multiplication(A,B):
#
#     C = [[0] * len(B[0]) for i in range(len(A))]
# # 遍历 A 的行
#     for i in range(len(A)): # len(A) 给出 A 的行数
# # 遍历 B 的列
#        for j in range(len(B[0])):
# # len(B[0]) 给出 B 的列数
# # 这一层相当于消去 k 所在的维度，即压缩
#           for k in range(len(B)):
#             C[i][j] += A[i][k] * B[k][j]
# # 完成对应元素相乘，再求和
#     return C
# # 定义矩阵 A 和 B
# A = [[1], [2], [3]]
# B = [[1, 2, 3]]
# print('A @ B = ')
# C = matrix_multiplication(A,B) # 调用自定义函数
# for row in C:
#     print(row)
# print('B @ A = ')
# D = matrix_multiplication(B,A) # 调用自定义函数
# for row in D:
#     print(row)
#

matrix = [[1 if i == j else 0 for i in range(4)]for j in range(4)]
# for row in matrix:
#     print(row)

#计算方阵的迹
def trace(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    if rows != cols:
       raise ValueError("Matrix is not square")
    diagonal_sum = sum(matrix[i][i] for i in range(rows))
    return diagonal_sum
# 示例用法
A = [[1, 2, 3],
[4, 5, 6],
[7, 8, 9]]
trace_A = trace(A)
trace_matrix = np.trace(matrix)
# print("矩阵的迹为:", trace_A, trace_matrix)


#判断是否为轴对称矩阵
# B = np.copy(matrix)
# B_T = B.T
# for i in range(B.shape[1]):
#     for j in range(B.shape[0]):
#         if B_T[i][j] == B[i][j]:
#             continue
#         else:
#             break
#     print("suit")



#矩阵行列式
C = np.array([[2, 3],
             [3, 2]])

C_res = np.linalg.det(C)

# print(C_res)

# 矩阵逆
C_res = np.linalg.inv(C)

print(C_res)

