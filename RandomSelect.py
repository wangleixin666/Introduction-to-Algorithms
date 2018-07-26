# coding:utf-8

"""
    第九章 随机选取，返回数组中第i小的元素
    采用快排中的思想，但是与快排不同的是，只处理划分的一边，而不是处理两边，期望时间复杂度是O(n)而不是O(nlgn)
"""
import random


def partition(array, p, r):
    # 快慢指针
    # 实现对子数组的原址重排，将q作为划分依据，左边都小于array[q]，右边都大于array[q]
    # q为划分标准的下标
    key = array[r]
    # 每次把最后一个元素当作主元
    i = p - 1
    for j in range(p, r):
        if array[j] <= key:
            i += 1
            # 确保i只有数组元素小于key时才移动，否则只移动j
            array[i], array[j] = array[j], array[i]
            # for循环结束时i代表数组中小于key的最后一个元素的下标
    array[i+1], array[r] = array[r], array[i+1]
    # 交换第一个大于key的元素和key保证了划分
    return i + 1


def random_partion(array, p, r):
    q = random.randint(p, r)
    # 随机选取基准的
    array[r], array[q] = array[q], array[r]
    return partition(array, p, r)


def random_select(array, p, r, i):
    # 返回array[p]到array[r]中第i小的元素
    if p == r:
        return array[p]
    q = random_partion(array, p, r)
    # array[p]到array[q-1]都小于array[q]
    # array[q+1]到array[r]都大于array[q]
    k = q - p + 1
    # 返回array[p]到array[q]中元素个数k个
    if i == k:
        return array[q]
    elif i < k:
        # 如果要找的最i小小于k个，那就在array[p]到array[q-1]中
        return random_select(array, p, q-1, i)
    else:
        return random_select(array, q+1, r, i-k)
        # 如果要找的第i小的个数大于k个，那就在array[q+1]到array[r]中，第k个最小，整体就是第k+i-k=i个小的元素
        # 因为array[p]到array[q-1]有k个元素都比array[q]小，所以只需要找array[q+1]到array[r]中第i-k小的的元素即可


if __name__ == "__main__":
    a = [2, 1, 3, 5, 4, 7]
    print random_select(a, 0, 5, 2)
