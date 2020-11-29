'''
Descripttion:  三角形的最大周长
version: 1
Author: Jason
Date: 2020-11-29 13:36:03
LastEditors: Jason
LastEditTime: 2020-11-29 14:31:19
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
    def largestPerimeter(self, A: List[int]) -> int:
        length = len(A)
        if length < 3:
            return 0
        A.sort()
        res = 0
        # 倒序遍历
        for i in range(length - 1, 1, -1):
            second = i - 1
            third = i - 2
            if second > -1 and third > -1:
                if A[second] + A[third] <= A[i]:
                    continue

                # if A[i] - A[second] >= A[third] or A[i] - A[third] > A[second] or A[second] - A[third] >= A[i]:
                if A[i] - A[third] > A[second]:
                    continue

                temp_sum = A[i] + A[second] + A[third]
                if temp_sum > res:
                    res = temp_sum
                    # 因为是从后往前遍历，所以找到的第一个就是最大的
                    break
        return res

    def largestPerimeter2(self, A: List[int]) -> int:
        if len(A) < 3:
            return 0
        from itertools import combinations
        res = 0
        for each in combinations(A, 3):
            # 任意两边之和大于第三边
            if each[0] + each[1] <= each[2]:
                continue
            elif each[1] + each[2] <= each[0]:
                continue
            elif each[0] + each[2] <= each[1]:
                continue

            # 任意两边之差小于第三边
            elif max(each[0], each[1]) - min(each[0], each[1]) >= each[2]:
                continue
            elif max(each[0], each[2]) - min(each[0], each[2]) >= each[1]:
                continue
            elif max(each[1], each[2]) - min(each[1], each[2]) >= each[0]:
                continue

            elif sum(each) > res:
                res = sum(each)
        return res


s = Solution()
for _ in range(100):
    li = GenerateRandomList(20, 30)
    res_stand = s.largestPerimeter2(li)
    res = s.largestPerimeter(li[::])
    if res != res_stand:
        print(li)
print("Done")
