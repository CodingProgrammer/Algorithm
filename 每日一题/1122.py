'''
Descripttion: 1122. 数组的相对排序
version: 1
Author: Jason
Date: 2020-11-14 10:27:51
LastEditors: Jason
LastEditTime: 2020-11-14 11:17:37
'''


from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        '''
        func: 循环遍历arr2中的每一个数，并在arr1中找到该数并弹出，添加到res数组中去。待arr2遍历完，arr1中仅剩独有的数，排序并合并数组
        param {arr1, arr2}
        return {list}
        '''
        res = list()
        nums = 0
        for each_num in arr2:
            while True:
                try:
                    index = arr1.index(each_num)
                    nums += 1
                    res.append(arr1.pop(index))
                except Exception as e:
                    break
        res.extend(sorted(arr1))
        return res

    def relativeSortArray2(self, arr1: List[int], arr2: List[int]) -> List[int]:
        '''
        func: 计数排序
        param {*}
        return {*}
        '''
        count_list = [0 for _ in range(1001)]
        res = list()
        # 统计arr1中每个数出现的次数
        for i in range(len(arr1)):
            count_list[arr1[i]] += 1
        # 使arr1中的数按照arr2的顺序排好
        for each_num in arr2:
            while count_list[each_num] > 0:
                res.append(each_num)
                count_list[each_num] -= 1
        # 对arr1中剩余的数添加到最后的结果数组中
        for i in range(len(count_list)):
            while count_list[i] > 0:
                res.append(i)
                count_list[i] -= 1
        return res


if __name__ == "__main__":
    s = Solution()
    arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
    arr2 = [2, 1, 4, 3, 9, 6]
    s.relativeSortArray2(arr1, arr2)
