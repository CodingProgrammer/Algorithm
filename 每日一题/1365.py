'''
Descripttion: 有多少小于当前数字的数字
version: 1
Author: Jason
Date: 2020-11-18 14:28:06
LastEditors: Jason
LastEditTime: 2020-11-18 14:48:13
'''
from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        '''
        func: 排序，如果元素在数组中唯一，则其下标即为前面比它小的个数；如果元素不唯一，排序后第一个该元素的下标即为前面比它小的个数
        param {list}
        return {list}
        '''
        location_dic = dict()
        res = list()
        temp_nums = sorted(nums)
        for i in range(len(nums)):
            current = i
            while current > 0 and temp_nums[current] == temp_nums[current - 1]:
                current -= 1
            location_dic[temp_nums[i]] = current
        for each_num in nums:
            res.append(location_dic[each_num])
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.smallerNumbersThanCurrent([7, 7, 7, 7]))
