'''
Descripttion: 移除元素
version: 1
Author: Jason
Date: 2020-11-19 22:19:11
LastEditors: Jason
LastEditTime: 2020-11-19 23:05:52
'''


from typing import List

import random


def GenerateRandomList(number, size):
    temp = [0] * random.randint(0, 10)
    random_legth = random.randint(0, size)
    current_length = 0
    while current_length < random_legth:
        temp.append(random.randint(1, number))
        current_length += 1
    random.shuffle(temp)
    return temp


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[fast], nums[slow] = nums[slow], nums[fast]
                slow += 1
        return slow

    def removeElement2(self, nums: List[int], val: int) -> int:
        p1 = 0
        p2 = 0
        length = len(nums)
        while p1 < length and p2 < length:
            while p1 < length and nums[p1] != val:
                p1 += 1

            while p2 < length and nums[p2] == val:
                p2 += 1

            if p1 < length and p2 < length:
                if p2 < p1:
                    p1, p2 = p2, p1
                else:
                    nums[p1], nums[p2] = nums[p2], nums[p1]
        for i in range(p2 - p1):
            nums.pop()
        return len(nums)

    def standad(self, nums: List[int], val: int):
        length_old = len(nums)
        num_equal = 0
        for each in nums:
            if each == val:
                num_equal += 1

        for _ in range(num_equal):
            nums.remove(val)
        return length_old - num_equal


if __name__ == "__main__":
    s = Solution()
    for i in range(10):
        li = GenerateRandomList(50, 20)
        value = 0
        print(s.removeElement(li, value))
