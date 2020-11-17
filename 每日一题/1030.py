'''
Descripttion: 距离顺序排列矩阵单元格
version: 1
Author: Jason
Date: 2020-11-17 14:46:38
LastEditors: Jason
LastEditTime: 2020-11-17 15:00:20
'''


from typing import List


class Solution:

    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        '''
        func: list排序的key
        param {*}
        return {*}
        '''
        location = [[i, j] for i in range(R) for j in range(C)]
        return sorted(location, key=lambda x: (abs(x[0] - r0) + abs(x[1] - c0)))


if __name__ == "__main__":
    s = Solution()
    R = 2
    C = 3
    r0 = 1
    c0 = 2
    print(s.allCellsDistOrder(R, C, r0, c0))
