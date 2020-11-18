'''
Descripttion: 单词倒排
version: 1
Author: Jason
Date: 2020-11-18 13:45:07
LastEditors: Jason
LastEditTime: 2020-11-18 13:46:31
'''
s_source = input()
res = list()
push_flag = False
s_temp = ''
for each_chr in s_source:
    if each_chr.isalpha():
        s_temp += each_chr
        push_flag = False
    else:
        if not push_flag and s_temp.isalpha():
            res.append(s_temp)
            push_flag = True
        s_temp = ''
if not push_flag and s_temp:
    res.append(s_temp)
print(" ".join(res[::-1]))
