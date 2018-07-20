# coding:utf-8

"""
    第二章 二分归并排序
    分治的思想，然后两部分子问题合并
    # 两种方法，递归和非递归的
    2.3.2 不使用哨兵，一旦左右某个数组的所有元素被写入数组中，则把另一个数组剩余的元素写入结果中
"""


def merge(A, B):
    # 合并AB两个已经排好序的list
    # 这种思路是先把短的加入到结果中，然后补充剩下的
    result = []
    m = 0
    n = 0
    len1 = len(A)
    len2 = len(B)
    while (m < len1) & (n < len2):
        if A[m] < B[n]:
            result.append(A[m])
            m += 1
        else:
            result.append(B[n])
            n += 1
    if m == len1:
        # 如果A比B短，然后把B剩下的直接加入到结果中
        for i in range(n, len2):
            result.append(B[i])
    else:
        for j in range(m, len1):
            result.append(A[j])
    return result


def mergesort(A):
    # 这里采用递归实现的
    if len(A) <= 1:
        return A
    p = 0
    q = len(A) - 1
    r = (p+q) / 2
    left = mergesort(A[p:r+1])
    right = mergesort(A[r+1:q+1])
    return merge(left, right)


"""
    还有一种非递归实现的方式
    非递归刚好相反：从最小子问题开始一步一步解决，直到复杂的问题
    
    i = 1
    while i < len(seq):
        print '子数组 长度 : ',i
        low = 0
        while low < len(seq):
            mid = low + i
            height = min(low + 2 * i, len(seq))
            if mid < height:
                print 'low ',low,'mid:',mid,'height:',height
                merge(seq,low,mid,height)
            low += 2*i
        i *= 2
    //非递归，自底向上
    public void mergeSortNonRecursion(Integer[] a) {
        //第一层循环 表示归并排序子数组的长度 从1 , 2 , 4 ,8 .....
        for(int i=1;i<a.length;i *= 2) {
            //第二层循环表示每两个自数组之间归并排序，确定起始和终止INDEX
            for(int low=0;low<a.length;low += 2*i) {
                merge(a, low, low + i- 1, Math.min(low + 2*i - 1, a.length - 1));
            }
        }
    }
"""


def mergesort_1(A):
    i = 1
    while i < len(A):
        # 外循环表示归并的子数组长度，从1,2,4,8.....每次乘2
        for j in range(0, len(A), 2*i):
            # 第二层循环表示子数组之间的归并排序，确定起始和终止的下标index
            A[j:j+2*i] = merge(A[j:j+i], A[j+i:j+2*i])
            # 注意更新为新的A，范围为新的
        i *= 2
    return A


if __name__ == "__main__":
    a = [2, 1, 3, 5, 4, 7]
    print mergesort_1(a)
