'''
Descripttion: 对链表进行插入排序
version: 1
Author: Jason
Date: 2020-11-20 10:03:56
LastEditors: Jason
LastEditTime: 2020-11-21 07:40:47
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
    def insertionSortList(self, head: ListNode) -> ListNode:

        if not head:
            return None
        dummy = ListNode(0)
        dummy.next = head
        cur = head
        while cur and cur.next:
            if cur.val <= cur.next.val:
                cur = cur.next

            else:
                temp = cur.next
                cur.next = cur.next.next
                pre = dummy

                while temp.val >= pre.next.val:
                    pre = pre.next
                temp.next = pre.next
                pre.next = temp

        return dummy.next

    def insertionSortList2(self, head: ListNode) -> ListNode:
        ans = ListNode(float("-inf"))

        while head:
            next = head.next
            cur = ans
            while cur.next and cur.next.val < head.val:
                cur = cur.next
            head.next = cur.next
            cur.next = head
            head = next
        return ans.next


if __name__ == "__main__":
    s = Solution()
    for _ in range(100):
        nums = GenerateRandomList(20, 10)
        if len(nums) < 1:
            continue
        nodes = [ListNode(each_num) for each_num in nums]
        sorted_nums = list(sorted(nums))
        # 连接链表
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        res = s.insertionSortList2(nodes[0])
        insertsort_li = list()
        cur = res
        while cur:
            insertsort_li.append(cur.val)
            cur = cur.next
        if insertsort_li != sorted_nums:
            print("wrong:", nums)
    print("Done")
    '''

    '''
