'''
Descripttion: 字母异位词分组
version: 1
Author: Jason
Date: 2020-12-14 14:04:42
LastEditors: Jason
LastEditTime: 2020-12-14 14:49:15
'''


from typing import List
import time


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        func: 超时
        param {*}
        return {*}
        '''
        res = list()
        for word in strs:
            for standards in res:
                if sorted(standards[0]) == sorted(word):
                    standards.append(word)
                    break
            else:
                res.append([word])
        return res

    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        res = dict()
        for word in strs:
            res.setdefault("".join(sorted(word)), []).append(word)
        return list(res.values())


s = Solution()
start = time.time()
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(s.groupAnagrams2(words))
end = time.time()
print(end - start)
