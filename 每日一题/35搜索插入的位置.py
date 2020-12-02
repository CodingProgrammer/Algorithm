'''
Descripttion: 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
你可以假设数组中无重复元素
version: 1
Author: Jason
Date: 2020-12-02 16:12:58
LastEditors: Jason
LastEditTime: 2020-12-02 16:55:47
'''

import random
from typing import List


def GenerateRandomList(number, size):
    temp = list()
    random_legth = random.randint(0, size)
    current_length = 0
    while current_length < random_legth:
        temp.append(random.randint(1, number))
        current_length += 1
    return temp


class Solution:
    def searchInsert(self, nums: List[int], target: int):
        length = len(nums)
        # 如果数组为空或者target比第一个数小
        if length < 1 or target <= nums[0]:
            return 0
        left = 0
        right = length - 1
        # 如果target比最后一个数大
        if target > nums[right]:
            return length
        # 二分法查找
        while left <= right:
            mid = left + ((right - left) >> 1)
            # 中间的数比target大，说明要找的target在mid的左侧
            if nums[mid] > target:
                right = mid - 1
            # 中间的数比target小，说明要找的target在mid的右侧
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        if left > right:
            return left

    def searchInsert2(self, nums: List[int], target: int):
        length = len(nums)
        # 如果数组为空或者target比第一个数小
        if length < 1 or target < nums[0]:
            return 0
        left = 0
        right = length - 1
        # 如果target比最后一个数大
        if target > nums[right]:
            return length
        try:
            return nums.index(target)
        except Exception as e:
            for i in range(length):
                if i > 0:
                    if nums[i - 1] < target and nums[i] > target:
                        return i


s = Solution()
# nums = [1, 2, 3, 5, 6, 8, 9, 11, 13, 14, 15, 17, 19]
# target = 1
# print(s.searchInsert(nums, target))
for _ in range(100):
    nums = list(set(GenerateRandomList(200, 200)))
    nums.sort()
    position = random.randint(0, len(nums) - 1)
    target = nums[position]
    res = s.searchInsert(nums, target)
    res_stand = s.searchInsert2(nums, target)
    if res != res_stand:
        print(nums)
        print(target)
print("Done")
