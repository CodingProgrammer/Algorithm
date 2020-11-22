'''
Descripttion: 面试题 10.01. 合并排序的数组
version: 1
Author: Jason
Date: 2020-11-22 14:12:38
LastEditors: Jason
LastEditTime: 2020-11-22 15:50:22
'''


from typing import List


class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        '''
        func: 反向双指针，先排最大的
        param {*}
        return {*}
        '''
        index = m + n - 1
        point_a = m - 1
        point_b = n - 1
        while point_a > -1 and point_b > -1:
            if A[point_a] >= B[point_b]:
                A[index] = A[point_a]
                point_a -= 1
            else:
                A[index] = B[point_b]
                point_b -= 1
            index -= 1

        while point_a > -1:
            A[index] = A[point_a]
            index -= 1
            point_a -= 1

        while point_b > -1:
            A[index] = B[point_b]
            index -= 1
            point_b -= 1

    def merge2(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify A in-place instead.
        """
        '''
        func: 先用temp把A拷贝出来。然后对temp和B利用双指针方法，将结果添加至A中
        param {*}
        return {*}
        '''
        temp = A[:m]
        p1 = 0
        p2 = 0
        index = 0
        while p1 < m and p2 < n:
            if temp[p1] <= B[p2]:
                A[index] = temp[p1]
                p1 += 1

            else:
                A[index] = B[p2]
                p2 += 1
            index += 1

        while p1 < m:
            A[index] = temp[p1]
            p1 += 1
            index += 1

        while p2 < n:
            A[index] = B[p2]
            index += 1
            p2 += 1

    def merge3(self, A: List[int], m: int, B: List[int], n: int) -> None:

        return sorted(A + B)
