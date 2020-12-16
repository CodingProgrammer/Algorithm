'''
Descripttion: 不同路径
version: 1
Author: Jason
Date: 2020-12-09 15:15:49
LastEditors: Jason
LastEditTime: 2020-12-09 16:53:32
'''


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1 for _ in range(m)]
        for i in range(1, n):
            for j in range(1, m):
                dp[j] += dp[j - 1]
        return dp[-1]

    def uniquePaths2(self, m: int, n: int) -> int:
        if m < 1 or n < 1:
            return 0
        dp = [[1 if (i == 0 or j == 0) else 0 for j in range(n)] for i in range(m)]
        for row in range(1, len(dp)):
            for column in range(1, len(dp[0])):
                dp[row][column] = dp[row - 1][column] + dp[row][column - 1]
        return dp[-1][-1]


s = Solution()
m = 7
n = 3
print(s.uniquePaths2(m, n))
