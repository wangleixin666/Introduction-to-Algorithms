#!/usr/bin/env python    # -*- coding: utf-8 -*
"""
    2.3.5 二分查找
    不再是顺序查找，而是分成两部分查找元素，前提是数组已经排好序了
"""


def binarysearch(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) / 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


A = [1, 3, 5, 7]
print binarysearch(A, input())

"""
# 如果不在数组中呢？
def BinarySearch(list, item):
    low = 0
    high = len(list) - 1

    for i in range(low, high):
        mid = (low + high) / 2
        if list[mid] > item:
            low = mid + 1
        elif list[mid] < item:
            high = mid - 1
        else:
            return list[mid]

# 缺少不在数组中的情况
def binarysearch(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) / 2
        # print mid
        if list[mid] > item:
            high = mid
            # print 'big'
        elif list[mid] < item:
            low = mid + 1
            # print 'small'
        else:
            return mid
            # 返回索引
"""

"""
readline()
n = sys.stdin.readline()
print len(n)
输入：abc
输出：4
原因：readline()会将标准输入的内容全部获取，包含最后的换行符，ASCII码十进制值为10
"""
"""
if __name__ == '__main__':
    try:
        while True:
            line = sys.stdin.readline().strip()
            if line == '':
                break
            lines = line.split()
            # item = input()
            # print item
            print binarysearch(lines, 3)
    except:
        pass

"""