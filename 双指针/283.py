'''
Descripttion: 移动零
version: 1
Author: Jason
Date: 2020-11-19 17:33:57
LastEditors: Jason
LastEditTime: 2020-11-19 19:30:51
'''
from typing import List
import random


def GenerateRandomList(number, size):
    temp = [0, 0, 0, 0]
    random_legth = random.randint(0, size)
    current_length = 0
    while current_length < random_legth:
        temp.append(random.randint(1, number))
        current_length += 1
    random.shuffle(temp)
    return temp


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if length < 2:
            return
        # p1是非零位置，p2是零位置
        p1 = 0
        p2 = 0

        while p1 < length and p2 < length:
            while p1 < length and nums[p1] != 0:
                p1 += 1

            while p2 < length and nums[p2] == 0:
                p2 += 1

            if p1 < length and p2 < length:
                if p2 < p1:
                    p1, p2 = p2, p1
                else:
                    nums[p1], nums[p2] = nums[p2], nums[p1]

    def moveZeroes2(self, nums: List[int]):
        noZeros = list()
        zeros = list()
        for each in nums:
            if each == 0:
                zeros.append(each)
            else:
                noZeros.append(each)
        noZeros.extend(zeros)
        return noZeros


if __name__ == "__main__":
    s = Solution()
    s.moveZeroes([11, 0, 4, 10, 20, 4, 13, 15, 13, 0, 10, 0, 0])
    for i in range(10):
        li = GenerateRandomList(20, 10)
        print("********************************************8")
        print(li)
        sorted_li = s.moveZeroes2(li)
        s.moveZeroes(li)
        if li != sorted_li:
            print("Wrong!")
