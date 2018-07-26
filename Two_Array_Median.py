# coding:utf-8

"""
    9.3.8 两个长度为n的有序数组，O(lgn)内找到2n个数的中位数
"""


def two_array_median(A, B):
    # 先来个暴力求解的方法O(nlgn)
    C = []
    for i in range(len(A)):
        C.append(A[i])
        C.append(B[i])
    C_sorted = sorted(C)
    # 时间复杂度为O(nlgn)
    if len(A) % 2 == 0:
        # 如果个数是奇数个，返回中间的
        result = C_sorted[len(A)]
    else:
        # 如果个数为偶数个，返回中间两个数的均值
        # 用2.0的话保证结果为小数
        result = (C_sorted[len(A)-1] + C_sorted[len(A)]) / 2.0
    return result


"""第二种方法是用归并的merge方法合并两个有序数组，并且长度一样为n，时间复杂度O(n)"""




def two_array_median_1(a, b):
    # 能达到时间复杂度为O(lgn)要求的
    # 肯定是分治算法
    if len(a) == 1:
        # 当只有一个值，中位数是两者的较小值
        return min(a[0], b[0])
    m = median_index(len(a))
    i = m + 1
    if a[m] < b[m]:
        return two_array_median_1(a[-i:], b[:i])
    else:
        return two_array_median_1(a[:i], b[-i:])


def median_index(n):
    if n % 2:
        return n // 2
    else:
        return n // 2 - 1


if __name__ == "__main__":
    a = [2, 4, 5]
    b = [1, 3, 7]
    print two_array_median_1(a, b)
