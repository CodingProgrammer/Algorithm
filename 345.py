'''
Descripttion: 反转字符串中的元音字母
version: 1
Author: Jason
Date: 2020-11-23 10:16:45
LastEditors: Jason
LastEditTime: 2020-11-23 10:23:33
'''


class Solution:
    def reverseVowels(self, s: str) -> str:
        words = list(s)
        left = 0
        right = len(words) - 1
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        while left < right:
            while left < right and words[left] not in vowels:
                left += 1

            while left < right and words[right] not in vowels:
                right -= 1

            if left < right:
                words[left], words[right] = words[right], words[left]
                left += 1
                right -= 1

        return "".join(words)


s = Solution()
string = "leetcode"
print(s.reverseVowels(string))
