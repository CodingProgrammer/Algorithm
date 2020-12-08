'''
Descripttion: 861. 翻转矩阵后的得分
version: 1
Author: Jason
Date: 2020-12-08 09:43:16
LastEditors: Jason
LastEditTime: 2020-12-08 10:15:19
'''


from typing import List


class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        '''
        func: 移动总共分为两步，首先观察一行，若以零开头，则移动完肯定会变大；之后观察每一列，若零比一多，则移动完会变大。
        param {*}
        return {*}
        '''
        # 检查行
        for row in range(len(A)):
            # 如果每一行的第一列为0，则对整行进行反转
            if A[row][0] == 0:
                for column in range(len(A[row])):
                    A[row][column] = 0 if A[row][column] else 1

        # 检查列-如果某一列存在的0比1多，则进行反转
        for column in range(len(A[0])):
            sum_column = sum([row[column] for row in A])
            if sum_column <= (len(A) // 2):
                for row in range(len(A)):
                    A[row][column] = 0 if A[row][column] else 1

        # 计算得分
        res = 0
        for row in A:
            row = [str(num) for num in row]
            res += int("".join(row), 2)
        return res


s = Solution()
li = [[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]
print(s.matrixScore(li))
