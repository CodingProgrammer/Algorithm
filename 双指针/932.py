'''
Descripttion: 922. 按奇偶排序数组 II
version: 1
Author: Jason
Date: 2020-11-12 11:14:52
LastEditors: Jason
LastEditTime: 2020-11-12 13:38:33
'''
from typing import List


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        '''
        func: 双指针法
        param {list}
        return {list}
        '''
        ou = 0
        ji = 1
        length = len(A)
        while ou < length and ji < length:
            while ou < length and A[ou] % 2 == 0:
                ou += 2
            if ou < length and ji < length:
                A[ou], A[ji] = A[ji], A[ou]

            while ji < length and A[ji] % 2 != 0:
                ji += 2
            if ou < length and ji < length:
                A[ji], A[ou] = A[ou], A[ji]
        return A

    def sortArrayByParityII2(self, A: List[int]) -> List[int]:
        '''
        func: 遍历一遍数组把所有的偶数放进 ans[0]，ans[2]，ans[4]，依次类推。
              再遍历一遍数组把所有的奇数依次放进 ans[1]，ans[3]，ans[5]，依次类推。
        param {list}
        return {list}
        '''
        list_ou = list()
        list_ji = list()
        res = list()
        for i in range(len(A)):
            if A[i] % 2:
                list_ji.append(A[i])
            else:
                list_ou.append(A[i])
        for i in range(len(list_ou)):
            res.append(list_ou[i])
            res.append(list_ji[i])
        return res


s1 = Solution()
print(s1.sortArrayByParityII2([2, 3, 2, 3]))
