'''
Descripttion: 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
version: 1
Author: Jason
Date: 2020-12-07 10:35:20
LastEditors: Jason
LastEditTime: 2020-12-07 16:10:25
'''


from typing import List
import random


def GenerateRandomList(number, size):
    temp = list()
    random_legth = random.randint(0, size)
    current_length = 0
    while current_length < random_legth:
        temp.append(random.randint(1, number))
        current_length += 1
    return temp


class Solution:
    def trap(self, height: List[int]):
        left = 0
        right = len(height) - 1
        lower = 0
        level = 0
        res = 0
        while left < right:
            if height[left] < height[right]:
                lower = height[left]
                left += 1
            else:
                lower = height[right]
                right -= 1
            level = lower if lower > level else level
            res += (level - lower)
        return res

    def trap2(self, height: List[int]):
        '''
        func: 按行求
        param {*}
        return {*}
        '''
        length = len(height)
        res = 0
        for index in range(1, length - 1):
            leftMax = 0
            for index_left in range(index):
                if height[index_left] > leftMax:
                    leftMax = height[index_left]
            rightMax = 0
            for index_right in range(index + 1, length):
                if height[index_right] > rightMax:
                    rightMax = height[index_right]
            lower = min(leftMax, rightMax)
            if lower > height[index]:
                res += (lower - height[index])
        return res

    def trap3(self, height: List[int]):
        '''
        func: 从左往右扫一遍，找到每一个值左侧的最大；从右往左扫一遍，找到每一个数右侧最大的值，
        param {*}
        return {*}
        '''
        length = len(height)
        if length < 3:
            return 0
        leftMax = [0]
        rightMax = [0]
        point_left = 1
        point_right = length - 2
        while point_left < length:
            # 添加leftMax
            if height[point_left - 1] > leftMax[-1]:
                leftMax.append(height[point_left - 1])
            else:
                leftMax.append(leftMax[-1])

            # 添加rightMax
            if height[point_right + 1] > rightMax[-1]:
                rightMax.append(height[point_right + 1])
            else:
                rightMax.append(rightMax[-1])

            point_left += 1
            point_right -= 1

        res = 0
        for i in range(length):
            lower = min(leftMax[i], rightMax[length - 1 - i])
            if lower > height[i]:
                res += (lower - height[i])
        return res


s = Solution()
for _ in range(100):
    li = GenerateRandomList(20, 20)
    if len(li) < 1:
        continue
    res1 = s.trap(li)
    res2 = s.trap2(li)
    res3 = s.trap3(li)
    if res1 != res3:
        print("*********************************")
        print("Wrong")
        print(li)
print("Done")
