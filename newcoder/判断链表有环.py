'''
Descripttion: 快慢指针
version: 1
Author: Jason
Date: 2020-12-08 14:31:08
LastEditors: Jason
LastEditTime: 2020-12-08 17:55:35
'''
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


from newcoder.合并有序链表 import ListNode
from typing import List


class Solution:
    def hasCycle(self, head):
        # write code here
        if not head:
            return False
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False
