'''
Descripttion: 回文链表
version: 1
Author: Jason
Date: 2020-11-24 16:20:33
LastEditors: Jason
LastEditTime: 2020-11-25 10:38:37
'''
# Definition for singly-linked list.
import random


def GenerateRandomList(number, size):
    temp = list()
    random_legth = random.randint(0, size)
    current_length = 0
    while current_length < random_legth:
        temp.append(random.randint(1, number))
        current_length += 1
    return temp


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode):
        # 特殊情况的返回
        if not head or not head.next:
            return True
        # 通过快慢指针，找到链表中间元素，并断开链表(previous.next = None)
        slow = head
        fast = head
        previous = None
        while fast and fast.next:
            previous = slow
            slow = slow.next
            if not fast or not fast.next:
                break
            fast = fast.next
            fast = fast.next
        cur = None
        # 如果链表的元素个数为偶数，则后半部分的头即为slow
        if not fast:
            cur = slow
        # 如果链表的元素个数为奇数，则后半部分的头为slow.next
        elif not fast.next:
            cur = slow.next
        previous.next = None
        # 反转后半部分的链表
        head_after = None
        while cur:
            temp = cur
            cur = cur.next
            temp.next = head_after
            head_after = temp
        # 依次对比反转后的链表和前半部分链表
        p1 = head
        p2 = head_after
        while p1 and p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next

        if not p1 and not p2:
            return True

        return False

    def isPalindrome2(self, head: ListNode):
        res = list()
        cur = head
        while cur:
            res.append(cur.val)
            cur = cur.next
        return res == res[::-1]


s = Solution()
choices = [True, False]
# print(s.isPalindrome([]))
for i in range(10):
    node_values = [1, 2, 3, 3, 2, 1]  # GenerateRandomList(10, 10)
    # flag = random.choice(choices)
    # if flag:
    #     node_values.extend(node_values[::-1])
    nodes = [ListNode(each_value) for each_value in node_values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    print(s.isPalindrome(nodes[0]))
