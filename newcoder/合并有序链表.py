'''
Descripttion: 双指针+伪指针
version: 1
Author: Jason
Date: 2020-12-08 17:45:52
LastEditors: Jason
LastEditTime: 2020-12-09 14:15:46
'''

import random


def GenerateRandomList(number, size):
    temp = [random.randint(0, number)]
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
    def mergeTwoLists(self, l1, l2):
        # write code here
        dummy = ListNode(float("inf"))
        cur = dummy
        p1, p2 = l1, l2
        while p1 and p2:
            if p1.val < p2.val:
                cur.next = p1
                p1 = p1.next
            else:
                cur.next = p2
                p2 = p2.next
            cur = cur.next
        # 有一个链表扫描完毕后，只需将目前的cur的next指向未扫描完的当前node即可，不用再while去扫描
        if p1:
            cur.next = p1
        else:
            cur.next = p2
        return dummy.next


s = Solution()
for _ in range(100):

    nums1 = GenerateRandomList(20, 20)
    nums2 = GenerateRandomList(20, 20)
    nums1.sort()
    nums2.sort()
    nums_stand = sorted(nums1 + nums2)
    nodes1 = [ListNode(num) for num in nums1]
    nodes2 = [ListNode(num) for num in nums2]
    nodes_stand = [ListNode(num) for num in nums_stand]

    for i in range(len(nums1) - 1):
        nodes1[i].next = nodes1[i + 1]

    for i in range(len(nums2) - 1):
        nodes2[i].next = nodes2[i + 1]

    for i in range(len(nums_stand) - 1):
        nodes_stand[i].next = nodes_stand[i + 1]

    res = s.mergeTwoLists(nodes1[0], nodes2[0])

    cur = nodes_stand[0]
    while cur:
        if cur.val != res.val:
            print("Wrong")
            print(nums1, nums2)
            break
        cur = cur.next
        res = res.next

    if cur or res:
        print("Wrong")
print("Done")
