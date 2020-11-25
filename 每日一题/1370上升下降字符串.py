'''
Descripttion: 1370. 上升下降字符串
version: 1
Author: Jason
Date: 2020-11-25 14:14:58
LastEditors: Jason
LastEditTime: 2020-11-25 14:15:14
'''


class Solution:
    def sortString(self, s: str) -> str:
        from collections import Counter
        myCount = Counter(s)
        reverse = False
        res = ""
        while sum(myCount.values()):
            temp = ''
            for k in sorted(myCount):
                if myCount[k] > 0:
                    temp += k
                    myCount[k] -= 1
            if reverse:
                res += temp[::-1]
                reverse = False
            else:
                res += temp
                reverse = True
        return res
