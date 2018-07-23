# coding:utf-8

"""
    4.1 最大连续子数组问题
    求带有正负数的数组中最大子数组的问题
    一是暴力求解法，二是分治思路
    还有动态规划算法。。。遇到为负则重新开始
"""


def max_subarray(list):
    # 暴力求解，时间复杂度为O(n^2)
    sum_max = float("-inf")
    # sum_Max代表全局最大的子数组和
    # 用负无穷表示最大，因为有可能全是负的，和为负数，比0小
    for i in range(len(list)):
        sum = 0
        # 用sum代表每次重新开始的和
        for j in range(i, len(list)):
            sum += list[j]
            if sum > sum_max:
                sum_max = sum
    return sum_max


def max_subarray_1(list, low, high):
    # 采用分治思想，时间复杂度为O(nlgn)
    # 可以看成是分成左右两部分，加上跨中间元素的组合部分
    mid = (low+high) / 2
    if low == high:
        return low, high, list[0]
    else:
        left_low, left_high, left_sum = max_subarray_1(a, low, mid)
        right_low, right_high, right_sum = max_subarray_1(a, mid+1, high)
        cross_low, cross_high, cross_sum = find_max_subarray(a, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum


def find_max_subarray(a, low, mid, high):
    # 求穿过mid中间项的最大连续子数组的和
    # 分为左右两个部分
    # 左边下标不断减小，右边不断增加
    left_sum = float("-inf")
    sum = 0
    max_left = 0
    for i in range(mid, low-1, -1):
        sum += a[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
    right_sum = float("-inf")
    sum = 0
    max_right = 0
    for j in range(mid+1, high+1):
        sum += a[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j
    return max_left, max_right, left_sum+right_sum


if __name__ == "__main__":
    a = [2, -1, 8, -3, 6, 0, 1]
    low = 0
    high = len(a) - 1
    print max_subarray_1(a, low, high)
    print max_subarray(a)
