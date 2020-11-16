'''
Descripttion: 16. 最接近的三数之和
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
version: 1
Author: Jason
Date: 2020-11-15 20:34:50
LastEditors: Jason
LastEditTime: 2020-11-16 09:33:40
'''


from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) < 3:
            return False
        res = -1
        diff = float("inf")
        length_nums = len(nums)
        nums.sort()
        for i in range(length_nums):
            left = i + 1
            right = length_nums - 1
            while left < right:
                temp_diff = nums[left] + nums[right] + nums[i] - target
                if abs(temp_diff) < diff:
                    diff = abs(temp_diff)
                    res = nums[left] + nums[right] + nums[i]
                if temp_diff < 0:
                    left += 1
                else:
                    right -= 1

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.threeSumClosest([3, 4, 5, 5, 7], 13))
