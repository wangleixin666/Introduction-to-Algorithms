# coding:utf-8

"""
    第六章 堆排序
    原址排序，只需要常数个额外空间，时间复杂度O(nlgn)
    分为建立最大堆的过程，维护堆的过程
    排序用最大堆，最小堆用来构建优先队列
    如果把堆看成是一棵树，堆中节点的高度就是该节点到叶节点的最长简单路径上边的数目
    维护堆的性质：逐级下降，使得下标为i的根节点重新遵循最大堆的性质
"""


def parent(i):
    return i/2


def left(i):
    # 因为是下标，i从0开始,子节点是1和2
    return 2*i + 1


def right(i):
    return 2*i + 2


def max_heapify(array, i, heap_size):
    # 插入第i个元素
    # 逐渐向下降，直到叶子节点，确保堆仍为最大堆
    # 这个过程的时间复杂度为O(lgn),lgn为树（堆）的高度
    l = left(i)
    r = right(i)
    largest = i
    if l < heap_size and array[l] > array[i]:
        # 注意<=取不到等号，否则会造成下标越界
        largest = l
    if r < heap_size and array[r] > array[largest]:
        # 此时最大已经为l和i代表的两个元素中较大的一个
        largest = r
    if largest != i:
        # 也就是说如果子节点中某个比子节点的大，则交换两个元素
        array[largest], array[i] = array[i], array[largest]
        max_heapify(array, largest, heap_size)
        # 然后更新最大堆


def build_max_heap(array):
    # 建立最大堆的时间复杂度是O(n)
    heap_size = len(array)
    for i in range((heap_size - 1)/2, -1, -1):
        # 从 (length - 1)/2 到 0 建立堆
        # 节点0就是最大堆的根节点，值是array[0]
        max_heapify(array, i, heap_size)


def heapsort(array):
    build_max_heap(array)
    heap_size = len(array)
    for i in range(len(array) - 1, 0, -1):
        # 这里都是下标，所以是从1到len-1，而下标为0的不用进行下一步的操作
        array[0], array[i] = array[i], array[0]
        heap_size -= 1
        max_heapify(array, 0, heap_size)
        # 不断维护最大堆，heap_size每次都是减少1个


# 迭代方式替换递归
def max_heapify_iter(A, i, heap_size):
    while True:
        # 否则就迭代进行维护最大堆的操作
        l = left(i)
        r = right(i)
        if l < heap_size and A[l] > A[i]:
            largest = l
        else:
            largest = i
        if r < heap_size and A[r] > A[largest]:
            largest = r
        if not largest == i:
            A[largest], A[i] = A[i], A[largest]
            i = largest
        else:
            # 也就是说插入的节点刚好最大，然后就不用向下进行更新最大堆的操作了
            break

""" 来源于：https://blog.csdn.net/zhang_xiaomeng/article/details/71703345 """
import math


class HeapSort:
    def __init__(self, a_A, a_heap_size):
        self.list = a_A
        self.heap_size = a_heap_size

    def parent(self, i):
        return math.floor((i-1)/2)

    def left(self, i):
        return 2*i + 1

    def right(self, i):
        return 2*i + 2

    def max_heapify(self, heap_size, A, i):
        largest = i
        key = A[i]
        # 先设定一个初始值，假如插入的最大

        l = self.left(i)
        r = self.right(i)
        if l < heap_size and A[l] > A[largest]:
            largest = l
        if r < heap_size and A[r] > A[largest]:
            largest = r
        A[i] = A[largest]
        A[largest] = key
        # 如果左右子节点某个比初始的largest大，则替换

        if largest != i:
            self.max_heapify(heap_size, A, largest)
            # 维护最大堆
        return A

    def build_max_heap(self, A):
        N = int(math.floor(len(A)/2) - 1)
        heap_size = len(A)
        for i in range(N, -1, -1):
            # 从n/2 - 1到0，因为是下标，要确保能够覆盖数组中全部的元素
            A = self.max_heapify(heap_size, A, i)
        return A

    def heapsort(self, A):
        # 原址进行堆排序
        self.build_max_heap(A)
        heap_size = len(A)
        for i in range(len(A)-1, 0, -1):
            A[0], A[i] = A[i], A[0]
            heap_size -= 1
            self.max_heapify(heap_size, A, 0)


if __name__ == "__main__":
    a = [2, 1, 3, 5, 4, 7]
    # hp = HeapSort(a, 6)
    # hp.heapsort(a)
    # print a
    # 这样才能完成排序
    # 而不是直接print hp.heapsort(a)
    # 因为没有返回值，原址进行排序了，相当于调用了sort，改变了a
    # sorted(a)
    # print a # a没有改变，而且sort是一个方法，调用为a.sort()
    heapsort(a)
    print a
