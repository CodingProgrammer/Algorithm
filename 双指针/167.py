'''
Descripttion: 两数之和 II - 输入有序数组
version: 1
Author: Jason
Date: 2020-11-14 11:43:12
LastEditors: Jason
LastEditTime: 2020-11-14 11:50:28
'''


from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        func: 双指针法
        param {*}
        return {*}
        '''
        left = 0
        right = len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1
        return False


if __name__ == "__main__":
    s = Solution()
    numbers = [2, 7, 11, 15]
    target = 9
    print(s.twoSum(numbers, target))
