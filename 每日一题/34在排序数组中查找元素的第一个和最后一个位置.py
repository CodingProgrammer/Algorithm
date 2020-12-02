'''
Descripttion: 34. 在排序数组中查找元素的第一个和最后一个位置
version: 1
Author: Jason
Date: 2020-12-01 16:12:21
LastEditors: Jason
LastEditTime: 2020-12-02 16:07:03
'''


from typing import List
import random


def GenerateRandomList(number, size):
    temp = list([0])
    random_legth = random.randint(0, size)
    current_length = 0
    while current_length < random_legth:
        temp.append(random.randint(1, number))
        current_length += 1
    return temp


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        if length < 1:
            return [-1, -1]
        left = 0
        right = length - 1
        first_index = -1
        last_index = -1
        while left <= right:
            mid = left + ((right - left) >> 1)
            if nums[mid] == target:
                first_index = mid
                break
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        if first_index == -1:
            return [-1, -1]
        # 向后找最大位置
        cur = first_index
        while cur < length and nums[cur] == target:
            last_index = cur
            cur += 1
        # 向前找最小位置
        cur = first_index
        while cur > -1 and nums[cur] == target:
            first_index = cur
            cur -= 1
        return [first_index, last_index]

    def searchRange2(self, nums: List[int], target: int) -> List[int]:
        if target in nums:
            first_index = nums.index(target)
            last_index = nums[::-1].index(target)
            if (first_index + last_index + 1) == len(nums):
                return [first_index, first_index]
            return [first_index, len(nums) - 1 - last_index]
        return [-1, -1]


s = Solution()
for _ in range(10):
    li = GenerateRandomList(20, 20)
    index_random = random.randint(0, len(li) - 1)
    times_random = random.randint(1, 5)
    li.extend([li[index_random]] * times_random)
    target = li[index_random]
    li.sort()
    res = s.searchRange(li, target)
    res_stand = s.searchRange2(li, target)
    if res != res_stand:
        print(li)
        print(target)
        print("Wrong")
print("Done")
