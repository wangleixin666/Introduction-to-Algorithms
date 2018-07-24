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


"""
动态规划策略：

从后往前分析：考虑加入第n的元素a[n]后的数组a[0--n]的最大子数组与加入前的数组a[0--n-1]的最大子数组之间的关系，找到状态转移的方程

它们的关系可能如下两种情况，
1.数组a[0--n]的最大子数组以a[n]元素结尾，可能由单个a[n]元素组成；
2.数组a[0--n]的最大子数组与a[n]无关，与数组a[0--n-1]的最大子数组相同。

若我们存储以a[n]元素结尾的最大子数组状态为end[n]，数组a[0--n]的最大子数组的状态为all[n]，

则得出状态转移方程如下:

end[n] = max(end[n-1] + array[n], array[n]);
all[n] = max(all[n-1], end[n]);

时间复杂度：只设计一次遍历：T(n)=O(n)。
"""


def max_subarray_2(array):
    end = []
    all = []
    end.append(float('-inf'))
    all.append(float('-inf'))
    for i in range(1, len(array)):
        end.append(max(end[i-1]+array[i-1], array[i-1]))
        all.append(max(end[i], all[i-1]))
        # 根据状态方程可以写出来，然后初始值为-inf
    print all
    return all[-1]


"""
  # 因为最大子列表一定是从一个非0的数开始的（假定列表中有正数有负数）
  # 所以就可以暂时筛选调小于0的数，即便列表全是负数，那么最大的子列表肯定是负数最大的一个
"""


def max_subarray_3(array):
    max_sum = array[0]
    pre_sum = 0
    # 临时的数组和，为负时重新开始
    for i in array:
        if pre_sum < 0:
            pre_sum = i
        else:
            pre_sum += i
        if pre_sum > max_sum:
            max_sum = pre_sum
            # 更新最大子数组和
    return max_sum


if __name__ == "__main__":
    a = [1, -2, 3, 10, -4, 7, 2, -5]
    low = 0
    high = len(a) - 1
    # print max_subarray_1(a, low, high)
    # print max_subarray(a)
    print max_subarray_2(a)
    print max_subarray_3(a)
