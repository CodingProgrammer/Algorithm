'''
Descripttion: 排序链表
version: 1
Author: Jason
Date: 2020-11-21 08:10:16
LastEditors: Jason
LastEditTime: 2020-11-21 11:48:00
'''
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
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        mid = self.getMid(head)
        right_head = mid.next
        mid.next = None

        left = self.sortList(head)
        right = self.sortList(right_head)

        return self.merge(left, right)

    def getMid(self, head: ListNode) -> ListNode:
        # 找到中点-slow
        slow = head
        fast = head
        # 通过以下while循环，找到链表的中点-slow
        while fast.next:
            if fast.next:
                fast = fast.next
            else:
                break
            if fast.next:
                fast = fast.next
            else:
                break
            slow = slow.next
        return slow

    def merge(self, left_head: ListNode, right_head: ListNode) -> ListNode:
        left_cur = left_head
        right_cur = right_head
        dummy_head = ListNode(float('-inf'))
        cur = dummy_head
        while left_cur and right_cur:
            if left_cur.val < right_cur.val:
                cur.next = left_cur
                left_cur = left_cur.next
            else:
                cur.next = right_cur
                right_cur = right_cur.next
            cur = cur.next
        cur.next = left_cur if left_cur else right_cur
        return dummy_head.next


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
        res = s.sortList(nodes[0])
        insertsort_li = list()
        cur = res
        while cur:
            insertsort_li.append(cur.val)
            cur = cur.next
        if insertsort_li != sorted_nums:
            print("wrong:", nums)
    print("Done")
    # li1 = [3, 1, 12, 6, 1, 9, 19, 4, 12]
    # li2 = [2, 4, 6, 8, 10]
    # nodes1 = [ListNode(each_num) for each_num in li1]
    # nodes2 = [ListNode(each_num) for each_num in li2]
    # # 连接链表
    # for i in range(len(nodes1) - 1):
    #     nodes1[i].next = nodes1[i + 1]
    # for j in range(len(nodes2) - 1):
    #     nodes2[j].next = nodes2[j + 1]
    # insertsort_li = list()
    # res = s.sortList(nodes1[0])
    # cur = res
    # while cur:
    #     insertsort_li.append(cur.val)
    #     cur = cur.next
    # if insertsort_li != sorted(li1):
    #     print("wrong:")
