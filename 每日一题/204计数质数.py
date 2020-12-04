'''
Descripttion: 204. 计数质数
version: 1
Author: Jason
Date: 2020-12-03 09:39:33
LastEditors: Jason
LastEditTime: 2020-12-04 14:31:03
'''


class Solution:
    def countPrimes(self, n: int):
        from math import sqrt, ceil
        if n < 3:
            return 0
        res = 1
        for i in range(3, n):
            # 大于2的偶数必不是质数，跳过
            if i % 2 == 0:
                continue
            isPrime = True
            for j in range(3, ceil(sqrt(i) + 1), 2):
                if i % j == 0:
                    isPrime = False
                    break
            if isPrime:
                res += 1
        return res

    def countPrimes2(self, n: int):
        primes = [1 for _ in range(n)]
        res = 0
        for i in range(2, n):
            if primes[i]:
                res += 1
                for j in range(i + i, n, i):
                    primes[j] = 0
        return res

    def countPrimes3(self, n: int):
        primes = [1 for _ in range(n)]
        res = 0
        for i in range(2, n):
            if primes[i]:
                res += 1
                for j in range(i * i, n, i):
                    primes[j] = 0
        return res


s = Solution()
print(s.countPrimes2(1500000))
# for i in range(100):
#     res = s.countPrimes(i)
#     res_stand = s.countPrimes2(i)
#     if res != res_stand:
#         print(i)
# print("Done")
