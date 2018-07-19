# coding:utf-8

"""
    第二章 插入排序
    原址排序，假定前面的序列已经排好了，然后依次从后向前比较，找到合适的插入位置
    将待排序的元素插入到指定位置
"""


def insertsort(list):
    for i in range(1, len(list)):
        temp = list[i]
        j = i-1
        while j >= 0 and list[j] > temp:
            list[j+1] = list[j]
            # 要有一个向后移位的操作
            j -= 1
        list[j+1] = temp
        # 最后确定位置了直接插入到该位置即可
    return list


if __name__ == "__main__":
    a = [2, 1, 3, 5, 4, 7]
    print insertsort(a)
