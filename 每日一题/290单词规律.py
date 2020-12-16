'''
Descripttion: pattern = "abba", str = "dog cat cat dog" -> true
version: 1
Author: Jason
Date: 2020-12-16 09:26:24
LastEditors: Jason
LastEditTime: 2020-12-16 17:39:39
'''


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mydict = dict()
        list_str = s.split(" ")
        if (len(pattern) != len(list_str)) or (len(set(pattern)) != len(set(list_str))):
            return False
        for index, chr in enumerate(pattern):
            res = mydict.setdefault(chr, list_str[index])
            if res != list_str[index]:
                return False
        return True

    def wordPattern2(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        return list(map(pattern.index, pattern)), list(map(s.index, s))


s = Solution()
pattern = "abba"
string = "dog cat cat dog"
print(s.wordPattern2(pattern, string))
