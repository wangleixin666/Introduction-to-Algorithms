# coding:utf-8

"""
    9.3.8 两个长度为n的有序数组，O(lgn)内找到2n个数的中位数
"""


def two_array_median(A, B):
    # 先来个暴力求解的方法O(nlgn)
    C = []
    for i in range(len(A)):
        C.append(A[i])
        C.append(B[i])
    C_sorted = sorted(C)
    # 时间复杂度为O(nlgn)
    result = (C_sorted[len(A)-1] + C_sorted[len(A)]) / 2.0
    return result


"""第二种方法是用归并的merge方法合并两个有序数组，并且长度一样为n，时间复杂度O(n)"""


def two_array_median_1(A, B):
    # 快慢数组，因为长度一样O(n)
    C = []
    i = 0
    j = 0
    while (i < len(A)) & (j < len(B)):
        if A[i] < B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1
    if i < len(A):
        for k in range(i, len(A)):
            C.append(A[k])
    if j < len(B):
        for k in range(j, len(B)):
            C.append(B[k])
    return (C[len(A)] + C[len(A) - 1]) / 2.0


def two_array_median_2(A, B):
    """
    能达到时间复杂度为O(lgn)要求的, 肯定是分治算法
    # 类似于折半查找的思想，因为两个数组有序，并且等长的
    # 可以换成找到两个合并后第k小，或者第k大的问题，以第k大为例子
    分析：
        取AB的中位数A[m/2],B[n/2]，比较大小，将AB分别分成A1，A2，B1，B2
        其中A1代表A[0....m/2-1]，A2代表A[m/2+1....m]
        同样B1代表B[0....n/2-1]，B2代表B[n/2+1....n]
        如果B的中位数更大，则A1<A[m/2]<B[n/2],而且B2<B[n/2]已经有m/2+1+n/2=t个数小于该值
        如果k <= t则要求的第k大的数肯定不在B2中
        如果k > t 则要求的数肯定不在A1中
        利用该规则，每次更新数组，总的时间复杂度为O(lg(m+n))
    """
    # 本题数组大小m和n相同，并且求的为中位数
    # 为了更新迭代的时候方便，将AB改成长度不一定一样的数组
    if len(A) == 1:
        # 当只有一个值，中位数是两者的平均值
        return (A[0] + B[0]) / 2.0
    if len(A) % 2 == 1:
        # AB长度为奇数时，中位数就是中间的
        m = (len(A) - 1) / 2
    else:
        # AB为偶数时，设定为中间两个数较小的一个
        m = len(A) / 2 - 1
    i = m + 1
    # 返回两者中位数的下标
    if A[m] < B[m]:
        # 比较两个数组的中位数大小
        # A的比B的小，则中位数肯定不在A1中，也就是A[0,i]
        # 注意这里是等长的两个数组，而且是中位数，不能简单地写成A[i:]和B
        return two_array_median_2(A[-i:], B[:i])
    else:
        return two_array_median_2(A[:i], B[-i:])


"""
def two_array_topk(A, B, k):
    # 寻找有序的AB两个数组中第k小的数
    if len(A) == len(B) == 1:
        return min(A[0], B[0])
        # 终止条件不对
        # 可能是用k，当k==1时，输出两者最小
        # 后面不断更新k的取值，反正就是二分的思想，不断丢掉一部分没用的数组
    m = midean(A)
    n = midean(B)
    t = m + n + 1
    if A[m] < B[n]:
        A, B = B, A
        # 确保A[m] > B[n]，否则就交换A，B
        # 仅仅是为了后续处理方便，没有实际含义
    if k <= t:
        # 肯定在A1,B1和A[m]中，因为比B[n]小的有t个
        return two_array_topk(A[:m+1], B[:n+1], k)
    else:
        # 肯定不在A1中
        return two_array_topk(A[m+1:], B[n+1:], k-t)


def midean(A):
    # 返回数组A中位数的下标m
    if len(A) % 2 == 1:
        # AB长度为奇数时，中位数就是中间的
        m = (len(A) - 1) / 2
    else:
        # AB为偶数时，设定为中间两个数较小的一个
        m = len(A) / 2 - 1
    return m
"""


def fun(nums1, nums2, k):
    # 两个有序数组中第k小的数
    if (len(nums2) + len(nums1)) < k:
        # 防患于未然
        return 'error, k大于两个list总个数'
    # 必须优先检查list是否为空,不然会越界...
    # 如果nums2为空,那么第k个元素,肯定是nums[k - 1]了啊(k - 1为序列第k个元素,是因为list从0开始...)
    if len(nums2) == 0:
        return nums1[k - 1]
    if len(nums2) > len(nums1):
        # 为了防止越界,保证nums1长度大于nums2
        # 不然就返回结果，重新赋值nums1和nums2
        return fun(nums2, nums1, k)
    # 取第一个元素,肯定是要比两个list的首个元素中比较小的那个
    # 单独列出来
    if k == 1:
        return min(nums1[0], nums2[0])
    # 防不胜防啊...因为nums2比nums1短,取k/2有可能越界...,检查了n久没查出来...
    # 如果nums2个数不足k/2，所以只能取比k/2小,又不越界的最大值了,即len(nums2),只要保证p + q = k就好啦...
    q = min(k / 2, len(nums2))
    p = k - q
    # p q的取值。。。。。
    if nums1[p - 1] < nums2[q - 1]:
        return fun(nums1[p:], nums2, k - p)
    elif nums1[p - 1] > nums2[q - 1]:
        return fun(nums1, nums2[q:], k - q)
    else:
        return nums1[p - 1]
        # 返回nums2[q - 1]也可以,反正一样大....

if __name__ == "__main__":
    a = [2, 4, 6]
    b = [1, 3, 5]
    print fun(a, b, 3)
    # print a[:2] # [2,4]
    # print a[:1], a[2:] # [2][4, 6]

