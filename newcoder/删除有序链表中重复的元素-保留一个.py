'''
Descripttion: 重复元素只保留一个
version: 1
Author: Jason
Date: 2020-12-08 17:01:11
LastEditors: Jason
LastEditTime: 2020-12-08 17:32:09
'''
import random


def GenerateRandomList(number, size):
    temp = [1, 2]
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
    def deleteDuplicates(self, head):
        '''
        func: 伪指针；cur,next1,next2
        param {*}
        return {*}
        '''
        if not head:
            return head
        dummy = ListNode(float("inf"))
        dummy.next = head
        cur = dummy
        while cur.next and cur.next.next:
            next1 = cur.next
            next2 = cur.next.next
            if next1.val != next2.val:
                cur = cur.next
            else:
                while next2 and next1.val == next2.val:
                    next2 = next2.next
                next1.next = next2
        return dummy.next


s = Solution()
for _ in range(100):
    nums = GenerateRandomList(20, 20)
    for _ in range(5):
        nums.append(random.choice(nums))
    nums.sort()
    nums_standard = sorted(set(nums))
    nodes_standard = [ListNode(num) for num in nums_standard]
    nodes = [ListNode(num) for num in nums]
    for i in range(len(nums) - 1):
        nodes[i].next = nodes[i + 1]

    for i in range(len(nums_standard) - 1):
        nodes_standard[i].next = nodes_standard[i + 1]

    res = s.deleteDuplicates(nodes[0])

    cur_stand = None
    if len(nodes_standard) >= 1:
        cur_stand = nodes_standard[0]
    cur_res = res
    while cur_stand:
        if cur_stand.val != cur_res.val:
            print("Wrong")
        cur_stand = cur_stand.next
        cur_res = cur_res.next
    if cur_res or cur_stand:
        print("Wrong")
print("Done")
