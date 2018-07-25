# coding:utf-8

"""
    6.5 优先队列
    如何基于最大堆实现优先队列
    优先队列是用来维护由一组元素构成的集合S的数据结构，其中每个元素都有一个相关的值，称为关键字key
    主要有以下几个操作：
    insert(S, x)将元素x插入到集合S中
    heap_maxmimum(S)返回S中具有最大关键字的元素
    heap_extract_max(S)去掉并返回S中的具有最大关键字的元素
    increase_key(S, x, k)将元素x的关键字值增加到k
    在一个n个元素的堆中，所有操作都能在O(lgn)内完成
"""


def parent(i):
    # 由于数组下标从0开始的问题，要更新parent函数
    return (i-1) / 2


def left(i):
    # 因为是下标，i从0开始,子节点是1和2
    return 2*i + 1


def right(i):
    return 2*i + 2


def max_heapify(array, i, heap_size):
    # 检查第i个元素,i为下标
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


def heap_maxmimum(S):
    # 返回具有最大关键字的元素
    return S[0]


def heap_extract_max(S):
    # 去掉并返回S中的具有最大关键字的元素
    # 类似于最大堆中交换A[i]和A[0]的操作
    heap_size = len(S)
    if heap_size < 1:
        print "heap underflow"
    max = S[0]
    S[0] = S[heap_size - 1]
    S.pop(heap_size - 1)
    heap_size -= 1
    max_heapify(S, 0, heap_size)
    return max


def increase_key(S, i, key):
    # 将元素i的关键字值增加到key，此时i是指最大堆中第i个元素
    if key < S[i]:
        print 'new key is smaller than current key'
    """
    S[i] = key
    while (i > 0) & (S[parent(i)] < S[i]):
        # 当某节点关键字增加时，另一支不相关的节点关键字应该没有变化
        S[i], S[parent(i)] = S[parent(i)], S[i]
        i = parent(i)
        # 因为此时S已经是最大堆了，只要比较i和父节点值就可以了，如果比它大就一直向上交换
        # 直到父节点是根节点，也就是当i等于1时
    """
    # 因为是一直交换，直到父节点比它大为止插入，所以可以用插入排序的思想
    while (i > 0) & (S[parent(i)] < key):
        S[i] = S[parent(i)]
        # 先都往后移
        i = parent(i)
    S[i] = key
    # 然后找到位置替换


def max_heap_insert(S, x):
    # 将元素x插入到集合S中
    # 先增加优先队列的长度，然后赋值为x
    heap_size = len(S)
    S.append(float('-inf'))
    # 此时使用list存储的，不能够用赋值操作，只能是append一个代表增加了一位
    increase_key(S, heap_size, x)


def heap_delete(S, i):
    # 删除堆中第i个元素
    heap_size = len(S)
    S[heap_size-1], S[i] = S[i], S[heap_size-1]
    # 交换掉要删除的元素和最后的元素，然后进行删除操作
    S.pop(heap_size-1)
    # 删除掉这个元素
    heap_size -= 1
    max_heapify(S, i, heap_size)


if __name__ == "__main__":
    a = [2, 1, 3, 5, 4, 7]
    build_max_heap(a)
    # print a # [7, 5, 3, 1, 4, 2]
    # 最大优先队列的建立依赖于最大堆，先对a建立最大堆，然后才能进行最大优先队列的操作
    # print heap_extract_max(a)
    # print a # [5, 4, 3, 1, 2, 2]
    # 此时a并没有减少长度，不过已经返回了最大值，并且更新堆了，所以采用类的话更有效果
    increase_key(a, 3, 8)
    print a # 对于increase_key(a, 3, 8)结果是[8, 7, 3, 5, 4, 2]
    # max_heap_insert(a, 2)
    # print a # [7, 5, 3, 2, 4, 2, 1]
    # heap_delete(a, 0)
    # print a # [5, 4, 3, 1, 2]
