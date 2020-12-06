'''
Descripttion: 118. 杨辉三角
version: 1
Author: Jason
Date: 2020-12-06 13:31:00
LastEditors: Jason
LastEditTime: 2020-12-06 13:40:18
'''


from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []

        elif numRows == 1:
            return [[1]]

        elif numRows == 2:
            return [[1], [1, 1]]

        else:
            res = [[1], [1, 1]]
            numRows -= 2
            while numRows > 0:
                temp = [1]
                for i in range(1, len(res[-1])):
                    temp.append(res[-1][i] + res[-1][i - 1])
                temp.append(1)
                res.append(temp)
                numRows -= 1
            return res


s = Solution()
print(s.generate(3))
