# coding:utf-8

"""
    2.2.2 选择算法（其实就是选择排序）
    将最小元素与A[1]交换，第二小和A[2]交换。。。。
"""


def selection(A):
    for i in range(len(A)):
        temp = A[i]
        # 把第i位存入临时变量temp准备交换用
        index = i
        # 设置最小元素下标为i
        for j in range(i+1, len(A)):
            if A[j] < A[index]:
                index = j
        # 此时下标index对应的元素为A[i]之后的最小元素
        A[i] = A[index]
        A[index] = temp
        # 交换两者
    return A


if __name__ == "__main__":
    a = [2, 1, 3, 5, 4, 7]
    print selection(a)
