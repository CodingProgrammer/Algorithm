'''
Descripttion: 两个数组的交集 II
version: 1
Author: Jason
Date: 2020-11-22 16:58:35
LastEditors: Jason
LastEditTime: 2020-11-22 16:59:35
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
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = list()
        nums1.sort()
        nums2.sort()
        p1 = 0
        p2 = 0
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] == nums2[p2]:
                res.append(nums1[p1])
                p1 += 1
                p2 += 1
            elif nums1[p1] < nums2[p2]:
                p1 += 1
            else:
                p2 += 1
        return res

    def intersect2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import defaultdict
        dict1 = defaultdict(int)
        dict2 = defaultdict(int)
        res = list()
        for each in nums1:
            dict1[each] += 1

        for each in nums2:
            dict2[each] += 1

        for each_key in dict1:
            if dict2[each_key] != 0:
                nums = min(dict1[each_key], dict2[each_key])
                res.extend([each_key] * nums)
        return res


s = Solution()
for _ in range(10):
    nums1 = GenerateRandomList(4, 12)
    nums2 = GenerateRandomList(4, 12)
    print(s.intersect2(nums1, nums2))
    print(s.intersect(nums1, nums2))
