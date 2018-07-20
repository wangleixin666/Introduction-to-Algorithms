# coding:utf-8

"""
    2.4 找数组中的逆序对
    也就是找到当前位置之后比当前位置小的元素构成一组
"""


def inversion(list):
    # 暴力求解，时间复杂度为O(n^2)
    number = 0
    for i in range(len(list)):
        for j in range(i, len(list)):
            if list[j] < list[i]:
                number += 1
                print (list[i], list[j])
    return number


def merge(A, B):
    # 合并AB两个已经排好序的list
    # 这种思路是先把短的加入到结果中，然后补充剩下的
    result = []
    m = 0
    n = 0
    len1 = len(A)
    len2 = len(B)
    while (m < len1) & (n < len2):
        if A[m] <= B[n]:
            result.append(A[m])
            m += 1
        else:
            result.append(B[n])
            n += 1
            global number
            # 把number设置为一个全局变量，然后每次加的时候都是累加的
            number += 1
            # 也就是说第一个数组中有比第二个大的逆序对就会加一
    if m == len1:
        # 如果A比B短，然后把B剩下的直接加入到结果中
        for i in range(n, len2):
            result.append(B[i])
    else:
        for j in range(m, len1):
            result.append(A[j])
    return result


def merge_inersion(A):
    # 这里采用递归实现的
    if len(A) <= 1:
        return A
    p = 0
    q = len(A) - 1
    r = (p+q) / 2
    left = merge_inersion(A[p:r+1])
    right = merge_inersion(A[r+1:q+1])
    return merge(left, right)


def inversion_2(data):
    # 将原来的数据进行排序
    # 排在它之后的原位置的元素个数就是逆序对数
    # 注意要用sorted排序，保留原来的位置
    sorted_data = sorted(data)
    count = 0
    for i in sorted_data:
        pos = data.index(i)
        count += pos
        data.pop(pos)
    return count

if __name__ == "__main__":
    number = 0
    # 在这里给全局变量number赋初值，然后进行归并的时候能够一直累加
    a = [2, 3, 8, 6, 1]
    merge_inersion(a)
    print number
