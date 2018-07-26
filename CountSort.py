# coding:utf-8

"""
    第八章 计数排序
    计数排序的思想就是对于每一个输入元素x，确定小于x的元素个数
    利用这一信息将元素直接放到数组中的位置
    # 基数排序，从最低位到最高位依次进行稳定排序
    # 桶排序，先对每个桶里的数进行排序，然后遍历每个桶，取出数字即可
"""


def countsort(array):
    B = [0 for i in range(len(array))]
    # B用来存放最终排序的结果
    C = [0 for i in range(0, max(array)+1)]
    # C存放的是0到最大值的范围内所有值出现的次数
    for i in range(len(array)):
        C[array[i]] += 1
    # print C # [0, 1, 1, 1, 1, 1, 0, 1]
    # 比如C[7] = 1 也就是说7出现了1次
    for i in range(1, max(array)+1):
        C[i] += C[i-1]
    # print C # [0, 1, 2, 3, 4, 5, 5, 6]
    # 现在C保存的是小于等于该值的元素个数，比如C[7]=6也就是说有6个元素小于等于7
    for j in range(len(array) - 1, -1, -1):
        B[C[array[j]] - 1] = array[j]
        # B和原数组array一样有6个数，但是下标最大为B[5]，所以会有溢出边界的问题
        # 这里只需要把B[C[array[j]]]改成B[C[array[j]] - 1]即可
        C[array[j]] -= 1
        # 与18行代码对应，将C[]恢复到初始值
    return B


if __name__ == "__main__":
    a = [2, 1, 3, 5, 4, 7]
    print countsort(a)
