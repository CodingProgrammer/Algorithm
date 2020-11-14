'''
Descripttion: 验证回文串
version: 1
Author: Jason
Date: 2020-11-13 10:35:06
LastEditors: Jason
LastEditTime: 2020-11-13 10:52:57
'''


class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        func: 双指针法
        param {*}
        return {*}
        '''
        left = 0
        right = len(s) - 1
        while left < right:
            # 判断左指针指向的是否为数字或者字母
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            # 如果为字母
            if s[left].isalpha():
                # 转换为大写，然后进行比较
                if s[left].upper() != s[right].upper():
                    return False
            # 如果为数字字符，直接比较
            else:
                if s[left] != s[right]:
                    return False
            left += 1
            right -= 1
        return True

    def isPalindrome2(self, s: str) -> bool:
        '''
        func: python处理字符串的方法
        param {*}
        return {*}
        '''
        res = ""
        # 循环遍历s，去除字符、数字之外的符号，且将字母均转换为大写
        for each_char in s:
            # 如果为数字，直接添加到res中
            if each_char.isdigit():
                res += each_char
            # 如果为字母，转换为大写后追加到res中
            elif each_char.isalpha():
                res += each_char.upper()
            else:
                pass
        return res == res[::-1]


s = Solution()
print(s.isPalindrome2("race a car"))
