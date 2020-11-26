'''
Descripttion: 164. 最大间距
version: 1
Author: Jason
Date: 2020-11-26 09:51:12
LastEditors: Jason
LastEditTime: 2020-11-26 22:51:10
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
    def maximumGap(self, nums: List[int]) -> int:
        length = len(nums)
        if length < 2:
            return 0
        max_num = max(nums)
        min_num = min(nums)
        # 每个桶的长度 (max-min) / (len(nums) - 1)
        each_bucket_length = max(1, (max_num - min_num) // (length - 1))
        # 桶的数量
        buckets_nums = (max_num - min_num) // each_bucket_length + 1
        # 创建桶，并将数字放置到相应桶内
        buckets = [[] for _ in range(buckets_nums)]
        for i in range(length):
            buckets[(nums[i] - min_num) // each_bucket_length].append(nums[i])
        pre_max = None
        res = 0
        for i in range(buckets_nums):
            if buckets[i] and pre_max:
                res = max(res, min(buckets[i]) - pre_max)

            if buckets[i]:
                pre_max = max(buckets[i])
        return res

    def maximumGap2(self, nums: List[int]) -> int:
        length = len(nums)
        if length < 2:
            return 0
        nums.sort()
        res = float("-inf")
        for i in range(length - 1):
            temp = nums[i + 1] - nums[i]
            if temp > res:
                res = temp
        return res


s = Solution()
for _ in range(100):
    li = GenerateRandomList(100, 40)
    res1 = s.maximumGap(li[::])
    res2 = s.maximumGap2(li[::])
    if res1 != res2:
        print("wrong")
        print(li)
print("Done")
