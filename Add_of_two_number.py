# coding:utf-8

"""
    2.1.4 把两个n位的二进制整数相加，用数组存储
    二进制相加要考虑进位的问题，也就是1+1 = 0，但是要进一位
    可以用于两个大数相加，在数组中存在一个进位的问题，如果二进制结果为2或者3，则进位
    然后顶位如果是有进位，则为1
    然后注意的是运算顺序是从右到左，其实就是从数组右边到左边，注意边界
"""

"""
类似问题：

二进制求和
给定两个二进制字符串，返回他们的和（用二进制表示）
# 这里没有说明是两个二进制字符的长度是否是相同的
样例
a = 11
b = 1
返回 100

解题：
和求两个链表的和很类似
考虑进位，考虑最后一项的进位

0+0 = 0 不需要进位
0+1 = 1 不需要进位
1+1 =0  进位 1

同时注意
低位进1，高位时1+1的情况，直接加就是3了，这个需要进位1 ，原位的结果也是1的情况
"""


def add_two_number(list1, list2):
    list = [0 for i in range(len(list1)+1)]
    # 存入最后的结果
    flag = 0
    # 代表进位
    for i in range(len(list1), 0, -1):
        # 加的话得从右往前，也就是从n到1
        list[i] = int(list1[i-1]) + int(list2[i-1]) + flag
        if list[i] > 1:
            list[i] -= 2
            flag = 1
        else:
            flag = 0
    if flag == 1:
        list[0] = 1
    return list


def addBinary_1(a, b):
    # 思路和上面的例题思路一样，不过是补充了字符串的长度
    # 这里的要求是ab和最后的结果都是字符串
    result = ''
    flag = 0
    # 代表进位
    max_length = 0
    len1 = len(a)
    len2 = len(b)
    # 因为没说是等长的字符串，所以要考虑长度的问题
    b_1 = ''
    a_1 = ''
    if len1 > len2:
        max_length = len1
        for i in range(len1-len2):
            b_1 += '0'
        b = b_1 + b
    if len2 > len1:
        max_length = len2
        for i in range(len2 - len1):
            a_1 += '0'
        a = a_1 + a
    if len1 == len2:
        max_length = len1
    # 到这里是补全位数，让ab等长，不够的前面补0

    # print 'a=', a
    # print 'b=', b
    # print max_length

    for i in range(max_length, 0, -1):
        # 然后采用补充长度后的共同长度进行相加操作
        if int(a[i - 1]) + int(b[i - 1]) + flag > 1:
            result = str(int(a[i - 1]) + int(b[i - 1]) + flag - 2) + result
            flag = 1
        else:
            result = str(int(a[i - 1]) + int(b[i - 1]) + flag) + result
            flag = 0
    if flag == 1:
        result = '1' + result
        # 如果首位为0则加一位1
    return result


def addBinary(a, b):
    # 这个思路还没看呢
    result = ''
    aLen = len(a) - 1
    bLen = len(b) - 1
    sum = 0
    while aLen >= 0 or bLen >= 0:
        if aLen >= 0:
            sum += int(a[aLen])
            aLen -= 1
        if bLen >= 0:
            sum += int(b[bLen])
            bLen -= 1
        if sum == 3:
            result = '1' + result
            sum = 1
        elif sum == 2:
            result = '0' + result
            sum = 1
        else:
            result = str(sum) + result
            sum = 0
    if sum == 1:
        result = '1' + result
    return result
if __name__ == "__main__":
    # list1 = raw_input().split(',')
    # list2 = raw_input().split(',')
    # print add_two_number(list1, list2)
    print addBinary_1('0', '0')

