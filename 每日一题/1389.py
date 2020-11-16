'''
Descripttion: 按既定顺序创建目标数组
version: 1
Author: Jason
Date: 2020-11-16 09:41:26
LastEditors: Jason
LastEditTime: 2020-11-16 13:32:54
'''


from typing import List


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        res = list()
        for i in range(len(nums)):
            res.insert(index[i], nums[i])
        return res


if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, 3, 4, 0]

    index = [0, 1, 2, 3, 0]
    s.createTargetArray(nums, index)
