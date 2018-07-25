# coding:utf-8

"""
    第七章 快速排序
    有额外的存储空间O(lgn)，时间复杂度为O(nlgn)和最坏的情况O(n^2)
    也是基于分治的思想，分为递归和非递归实现两种方式
"""
import random


def partition(array, p, r):
    # 快慢指针？
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
    # 随机选择划分点key，而不是固定的最后一位
    i = random.randint(p, r)
    array[r], array[i] = array[i], array[r]
    # 其实还可以用到原来的方法中。。。。
    return partition(array, p, r)


def quicksort(array, p, r):
    if p < r:
        # q = partition(array, p, r)
        # print q # 3,2,0,4
        q = random_partion(array, p, r)
        # print q
        quicksort(array, p, q-1)
        # 从p到q-1全部小于array[q]
        quicksort(array, q+1, r)
        # 从q+1到r全部大于array[q]


def quicksort_1(array):
    # 简单写法，其实时间复杂度是一样的，都是遍历一遍数组并递归
    if not len(array):
        return []
    else:
        # 在这里以第一个元素为基准线
        pivot = array[0]
        left = quicksort_1([x for x in array[1:] if x < pivot])
        # 所有小于基准的放左边，大于基准的放右边，然后进行递归
        right = quicksort_1([x for x in array[1:] if x >= pivot])
    return left + [pivot] + right


"""
    还有一个非递归实现的快速排序版本
    利用栈的思想，将需要继续排序的首尾下标存入栈中，不断弹栈进行分区操作
    
    1.申请一个栈，存放排序数组的起始位置和终点位置。
    2.将整个数组的起始位置start和终点位置end进栈
    3.出栈数据，对出栈的数据进行排序，查找基准数据所在最终的位置 pivot。
    4.判断起始位置start是否小于基准位置pivot-1，如果小于则将起始位置和pivot-1为终点位置进栈
    5.判断基准位置pivot+1 是否小于终点位置end,如果小于则将 pivot+1作为起始位置，end作为终点位置进栈
    6.判断栈是否为空，如果不为空则重复第三步，否则退出操作
"""


def quicksort_2(array, l, r):
    if l >= r:
        return
    stack = []
    stack.append(l)
    stack.append(r)
    # 将起始位置和终止位置进栈
    while stack:
        low = stack.pop(0)
        high = stack.pop(0)
        # 出栈初始位置和终止位置
        if high - low <= 0:
            # 有一个终止条件，和 l >= r 条件一样？
            continue
        x = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] <= x:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[high] = array[high], array[i + 1]
        # 划分基准位置的操作和partion一样
        # i+1为返回的基准位置
        stack.extend([low, i, i + 2, high])


def quicksort_3(arr):
    if len(arr) < 2:
        return arr
    stack = []
    stack.append(len(arr)-1)
    stack.append(0)
    # 进栈初始位置和结束位置
    while stack:
        l = stack.pop()
        r = stack.pop()
        index = partition(arr, l, r)
        # index相当于i+1，也就是基准位置
        if l < index - 1:
            # index-1相当于比基准位置小的元素位置
            stack.append(index - 1)
            stack.append(l)
        if r > index + 1:
            # index+!也就是比基准位置大的元素位置
            stack.append(r)
            stack.append(index + 1)


if __name__ == "__main__":
    a = [2, 1, 3, 5, 7, 4]
    # quicksort(a, 0, 5)
    # print a
    # quicksort_2(a, 0, 5)
    quicksort_3(a)
    print a


