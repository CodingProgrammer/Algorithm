'''
Descripttion: 环形链表
version: 1
Author: Jason
Date: 2020-11-24 11:14:17
LastEditors: Jason
LastEditTime: 2020-11-24 14:03:09
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
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        slow = head
        fast = head
        while slow or fast:
            slow = slow.next
            fast = fast.next
            if not fast or not fast.next:
                break
            fast = fast.next
            if slow == fast:
                return True
        return False


s = Solution()
for i in range(10):
    node_values = GenerateRandomList(10, 10)
    print("**********************************************")
    print(node_values)
    nodes = [ListNode(each_value) for each_value in node_values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    flag = random.randint(0, 1)
    pos = None
    if flag:
        pos = random.randint(0, len(node_values) - 1)
        nodes[-1].next = nodes[pos]
    print("flag: %s    pos: %4s     hasCircle: %s" % (flag, pos, s.hasCycle(nodes[0])))
