# coding:utf-8

"""
    6.5.9 在O(nlgk)时间复杂度合并k个有序链表
    算法导论提示使用k个最小堆完成k路归并
    思路：遍历k个链表的话，时间复杂度过大O(nk)，然后排序O(nklg(nk))
    利用了最小堆的数据结构
    首先把k个链表的首元素都加入最小堆中，它们会自动排好序
    然后我们每次取出最小的那个元素加入我们最终结果的链表中
    然后把取出元素的下一个元素再加入堆中，下次仍从堆中取出最小的元素做相同的操作
    以此类推，直到堆中没有元素了，此时k个链表也合并为了一个链表，返回首节点即可
    还没有完成
"""


def left(i):
    # 因为是下标，i从0开始,子节点是1和2
    return 2*i + 1


def right(i):
    return 2*i + 2


def min_heapify(array, i, heap_size):
    # 最小堆
    l = left(i)
    r = right(i)
    smallest = i
    if l < heap_size and array[l] < array[i]:
        smallest = l
    if r < heap_size and array[r] < array[smallest]:
        smallest = r
    if smallest != i:
        array[smallest], array[i] = array[i], array[smallest]
        min_heapify(array, smallest, heap_size)


def build_min_heap(array):
    # 建立最小堆的时间复杂度是O(n)
    heap_size = len(array)
    for i in range((heap_size - 1)/2, -1, -1):
        # 从 (length - 1)/2 到 0 建立堆
        # 节点0就是最大堆的根节点，值是array[0]
        min_heapify(array, i, heap_size)


def merge_lists(list):
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


"""leetcode暴力求解方法"""


class ListNode(object):
    # python中定义链表
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        self.nodes = []
        head = point = ListNode(0)
        for l in lists:
            while l:
                self.nodes.append(l.val)
                l = l.next
        for x in sorted(self.nodes):
            point.next = ListNode(x)
            point = point.next
        return head.next

    def mergeKLists_1(self, lists):
        output = []
        for i in range(0, len(lists)):
            curr = lists[i]
            while curr:
                output.append(curr.val)
                curr = curr.next
        return sorted(output)

if __name__ == "__main__":
    for i in range(3):
        list_i = raw_input().split(',')
        print list_i
        # Solution().mergeKLists(lists)
