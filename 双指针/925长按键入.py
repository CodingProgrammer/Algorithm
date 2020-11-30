'''
Descripttion: 925. 长按键入
version: 1
Author: Jason
Date: 2020-11-30 10:54:51
LastEditors: Jason
LastEditTime: 2020-11-30 12:09:32
'''


class Solution:
    def isLongPressedName(self, name: str, typed: str):
        '''
        func: 先是name和typed共同前进，如果遇到不同字符，再对typed进行去重（如果typed的指针所指与前面的字符相同，则指针后移一位）
        param {*}
        return {*}
        '''
        length_name = len(name)
        length_typed = len(typed)
        index_name = 0
        index_typed = 0
        while index_name < length_name and index_typed < length_typed:
            if name[index_name] != typed[index_typed]:
                return False
            previous_typed = None
            # 如果相同，同时后移
            while index_name < length_name and index_typed < length_typed and name[index_name] == typed[index_typed]:
                index_name += 1
                previous_typed = index_typed
                index_typed += 1
            # typed去重
            while index_typed < length_typed and typed[index_typed] == typed[previous_typed]:
                previous_typed = index_typed
                index_typed += 1
        if index_name == length_name and index_typed == length_typed:
            return True
        return False


s = Solution()
name = "laiden"
typed = "laiden"
print(s.isLongPressedName(name, typed))
