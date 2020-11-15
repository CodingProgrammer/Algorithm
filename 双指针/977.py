'''
Descripttion: 977. 有序数组的平方
version: 1
Author: Jason
Date: 2020-11-15 13:29:17
LastEditors: Jason
LastEditTime: 2020-11-15 15:22:05
'''
from typing import List


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        left = 0
        right = len(A) - 1
        res = list()
        while left <= right:
            if abs(A[left]) > abs(A[right]):
                res.append(A[left] * A[left])
                left += 1
            else:
                res.append(A[right] * A[right])
                right -= 1
        return res[::-1]

    def sortedSquares2(self, A: List[int]) -> List[int]:
        '''
        func: 利用sorted函数的key解决
        param {*}
        return {*}
        '''
        return [x * x for x in sorted(A, key=abs)]


if __name__ == "__main__":
    s = Solution()
    print(s.sortedSquares([-7, -3, 2, 3, 11]))
