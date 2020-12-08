'''
Descripttion: 反转链表
version: 1
Author: Jason
Date: 2020-12-08 14:24:37
LastEditors: Jason
LastEditTime: 2020-12-08 17:54:27
'''

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead:
            return pHead
        pre_node = None
        next_node = None
        while pHead:
            next_node = pHead.next
            pHead.next = pre_node
            pre_node = pHead
            pHead = next_node
        return pre_node

    def ReverseList2(self, pHead):
        # 用了额外的内存空间
        if not pHead:
            return pHead
        cur = pHead
        nodes = list()
        while cur:
            nodes.append(cur)
            cur = cur.next
        for i in range(len(nodes) - 1, 0, -1):
            nodes[i].next = nodes[i - 1]
        nodes[0].next = None
        return nodes[-1]
