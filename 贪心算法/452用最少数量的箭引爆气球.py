'''
Descripttion: 用最少数量的箭引爆气球
version: 1
Author: Jason
Date: 2020-11-24 14:40:10
LastEditors: Jason
LastEditTime: 2020-11-24 16:00:31
'''

import random
from typing import List


def GenerateRandomList(left_bound, right_bound, numbers):
    temp = list()
    random_legth = random.randint(0, numbers)
    current_length = 0
    while current_length < random_legth:
        left_point = random.randint(0, left_bound)
        right_point = random.randint(left_point + 1, right_bound)
        temp.append([left_point, right_point])
        current_length += 1
    return temp


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda point: point[1])
        arrows = 0
        boundary = float("-inf")
        for point in points:
            if point[0] > boundary:
                arrows += 1
                boundary = point[1]
        return arrows

    def findMinArrowShots2(self, points: List[List[int]]) -> int:
        '''
        func: 按开始位置排序，维护gap区域，如果当前点不在gap范围内，则arrows+1，且将gap更新为当前点的区间
        param {*}
        return {*}
        '''
        if len(points) < 1:
            return 0
        points.sort()
        arrows = 1
        gap = [float("-inf"), float("inf")]
        for each in points:
            if gap[0] <= each[0] <= gap[1] or gap[0] <= each[1] <= gap[1]:
                gap = [max(gap[0], each[0]), min(gap[1], each[1])]
                continue
            gap = each
            arrows += 1
        return arrows


s = Solution()
for i in range(100):
    points = GenerateRandomList(30, 60, 20)
# print("**********************************************")
# print(points)
    points2 = points[::]
    res = s.findMinArrowShots(points[::])
    res2 = s.findMinArrowShots2(points2)
    # print("res: %d     res2: %d" % (res, res2))
    if res != res2:
        print("***************************************")
        print(points)
        print("Wrong")
print("Done!")
