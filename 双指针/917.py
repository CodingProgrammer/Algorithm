'''
Descripttion: 917. 仅仅反转字母
version: 1
Author: Jason
Date: 2020-11-14 11:19:56
LastEditors: Jason
LastEditTime: 2020-11-14 11:32:12
'''


class Solution:
    def reverseOnlyLetters(self, S: str):
        '''
        func: 双指针法
        param {*}
        return {*}
        '''
        left = 0
        right = len(S) - 1
        li = list(S)
        while left < right:
            while left < right and (not li[left].isalpha()):
                left += 1
            while left < right and (not li[right].isalpha()):
                right -= 1
            if left < right:
                li[left], li[right] = li[right], li[left]
                left += 1
                right -= 1
        return "".join(li)


if __name__ == "__main__":
    s = Solution()
    print(s.reverseOnlyLetters("-S2,_"))
