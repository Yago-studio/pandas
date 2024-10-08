
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
for row in matrix:
    print(row)

