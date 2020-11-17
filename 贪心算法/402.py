'''
Descripttion: 402. 移掉K位数字
version: 1
Author: Jason
Date: 2020-11-17 07:34:51
LastEditors: Jason
LastEditTime: 2020-11-17 14:08:57
'''


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        res = list()
        for i in range(len(num)):
            while len(res) > 0 and int(num[i]) < int(res[-1]) and k > 0:
                res.pop()
                k -= 1
            # ! 往栈里添加数字，如果只有 num[i] != 0，会导致200后面的0无法进栈
            if len(res) != 0 or num[i] != '0':
                res.append(num[i])
        while len(res) > 0 and k > 0:
            res.pop()
            k -= 1
        if len(res) == 0:
            return '0'
        return "".join(res)


if __name__ == "__main__":
    s = Solution()
    resq = s.removeKdigits(num="12345", k=2)
    print(resq)
