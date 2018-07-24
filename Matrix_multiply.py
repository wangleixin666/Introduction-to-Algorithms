# coding:utf-8

"""
    4.2 矩阵相乘
    矩阵乘法，n*n 的矩阵AB相乘返回结果n*n的矩阵C
"""


def matrix_multiply(A, B):
    n = len(A)
    C = [[0 for i in range(n)]for j in range(n)]
    # 初始化一个全为0的n*n 的二维数组（矩阵）
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C


def matrix_multiply_1(A, B):
    # 采用分治的思路，如果矩阵的规模大于等于2，把矩阵分解成为4个n/2的子矩阵相乘，然后求和
    n = len(A)
    m = int(n/2)
    C = [[0 for i in range(2)]for j in range(2)]
    # 初始化一个全为0的n*n 的二维数组（矩阵）
    if n == 1:
        C[0][0] = A[0][0] * B[0][0]
    else:
        a11 = [[0 for i in range(m)] for j in range(m)]
        b11 = [[0 for i in range(m)] for j in range(m)]
        for i in range(m):
            for j in range(m):
                a11[i][j] = A[i][j]
                b11[i][j] = B[i][j]
        a12 = [[0 for i in range(m)] for j in range(m)]
        b12 = [[0 for i in range(m)] for j in range(m)]
        for i in range(m):
            for j in range(m):
                a12[i][j] = A[i+m][j]
                b12[i][j] = B[i+m][j]
        a21 = [[0 for i in range(m)] for j in range(m)]
        b21 = [[0 for i in range(m)] for j in range(m)]
        for i in range(m):
            for j in range(m):
                a21[i][j] = A[i][j+m]
                b21[i][j] = B[i][j+m]
        a22 = [[0 for i in range(m)] for j in range(m)]
        b22 = [[0 for i in range(m)] for j in range(m)]
        for i in range(m):
            for j in range(m):
                a22[i][j] = A[i+m][j+m]
                b22[i][j] = B[i+m][j+m]
        # 完成了矩阵分割，然后就是递归的求解
        C[0][0] = matrix_multiply_1(a11, b11) + matrix_multiply_1(a12, b21)
        C[0][1] = matrix_multiply_1(a11, b12) + matrix_multiply_1(a12, b22)
        C[1][0] = matrix_multiply_1(a21, b11) + matrix_multiply_1(a22, b21)
        C[1][1] = matrix_multiply_1(a21, b12) + matrix_multiply_1(a22, b22)
        C = [[C[0][0], C[0][1]], [C[1][0], C[1][1]]]
    return C

if __name__ == "__main__":
    a = [[2, 1, 1, 3], [1, 2, 3, 1], [1, 3, 2, 1], [3, 1, 2, 1]]
    b = [[1, 2, 3, 1], [2, 1, 3, 1], [3, 1, 2, 1], [1, 3, 2, 1]]
    # print type(a) # <type 'list'>
    print matrix_multiply_1(a, b)
