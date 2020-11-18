'''
Descripttion: 字符串排序
version: 1
Author: Jason
Date: 2020-11-18 13:51:35
LastEditors: Jason
LastEditTime: 2020-11-18 13:51:43
'''
while True:
    try:
        s = input()
        myStack = list()
        special = list()
        for i, each_chr in enumerate(s):
            # 如果是字母
            if each_chr.isalpha():
                # 如果mystack不为空
                if len(myStack):
                    # 最后一个字符位置
                    compare = len(myStack) - 1
                    while compare >= 0 and not myStack[compare].isalpha():
                        compare -= 1
                    while compare >= 0 and myStack[compare].isalpha() and ord(myStack[compare].upper()) > ord(each_chr.upper()):
                        compare -= 1
                    myStack.insert(compare + 1, each_chr)

                else:
                    myStack.append(each_chr)
            # 如果不是字母,添加到辅助数组special
            else:
                special.append((i, each_chr))
        for each in special:
            myStack.insert(each[0], each[1])
        print("".join(myStack))
    except Exception as e:
        break
