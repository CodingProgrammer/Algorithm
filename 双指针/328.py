'''
Descripttion:  奇偶链表
version: 1
Author: Jason
Date: 2020-11-13 10:12:03
LastEditors: Jason
LastEditTime: 2020-11-13 10:19:03
'''
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        '''
        func: 给定一个单链表，把所有的奇数节点和偶数节点分别排在一起
        param {head}
        return {head}
        '''
        # 如果链表为空，或者长度为1（只有头），则返回
        if not head or not head.next:
            return head
        # 保存头
        odd_head = head
        even_head = odd_head.next

        odd_temp = odd_head
        even_temp = even_head
        # 如果当前odd或者even节点的next为空， 则退出循环
        while odd_temp.next and even_temp.next:
            # 当前odd节点的next指向even节点的next（即下一个odd），且更新odd的位置
            odd_temp.next = even_temp.next
            odd_temp = even_temp.next
            # 如果odd的next存在，则更新even的next节点，并更新even的位置
            if odd_temp.next:
                even_temp.next = odd_temp.next
                even_temp = odd_temp.next
            # 如果odd的next为None，说明到头了，将even的next置空，退出循环
            else:
                even_temp.next = None
                break
        # 退出循环之后，说明odd链表和even链表都重新组装好了，将odd的next指向even的头即可
        odd_temp.next = even_head
        return odd_head
