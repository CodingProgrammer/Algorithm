'''
Descripttion: 求小球落地5次后所经历的路程和第5次反弹的高度
version: 1
Author: Jason
Date: 2020-11-20 14:02:19
LastEditors: Jason
LastEditTime: 2020-11-20 14:18:39
'''
altitude = int(input())
distance = 0
distance_rep = 0
for _ in range(5):
    distance += altitude + distance_rep
    altitude = altitude / 2
    distance_rep = altitude
print(distance)
print(distance_rep)
