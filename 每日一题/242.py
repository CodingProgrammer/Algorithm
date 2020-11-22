'''
Descripttion: 有效的字母异位词
version: 1
Author: Jason
Date: 2020-11-22 11:00:30
LastEditors: Jason
LastEditTime: 2020-11-22 11:09:50
'''


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        return Counter(s) == Counter(t)
        pass


s = "rat"
t = "car"
print(sorted(s) == sorted(t))
