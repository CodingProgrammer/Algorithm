'''
Descripttion: 链表中倒数第k个节点
version: 1
Author: Jason
Date: 2020-11-20 12:08:11
LastEditors: Jason
LastEditTime: 2020-11-20 13:42:23
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
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        fast = head
        slow = head
        while k > 0:
            fast = fast.next
            k -= 1

        while fast:
            fast = fast.next
            slow = slow.next
        return slow

    def getKthFromEnd2(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        # 首先算出链表的总长度
        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next

        cur = head
        times = length - k
        while times > 0:
            cur = cur.next
            times -= 1

        return cur


if __name__ == "__main__":
    s = Solution()
    for _ in range(100):
        nums = GenerateRandomList(20, 10)
        if len(nums) < 1:
            continue
        nodes = [ListNode(each_num) for each_num in nums]
        # 连接链表
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        k = random.randint(1, len(nums))
        if s.getKthFromEnd(nodes[0], k).val != nums[-k]:
            print("Wrong:", nums)
    print("Done!")
    '''
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5

    print(s.getKthFromEnd(n1, 3).val)
    '''
