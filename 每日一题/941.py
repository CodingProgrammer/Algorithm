'''
Descripttion: 941. 有效的山脉数组
version: 1
Author: Jason
Date: 2020-11-15 15:28:53
LastEditors: Jason
LastEditTime: 2020-11-15 16:09:41
'''


from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        '''
        func: 先找到最大的数，然后分别向左和向右遍历，找出不符合排序规则的数，若没有，则为True
        param {*}
        return {*}
        '''
        if len(arr) < 3:
            return False
        # 找到数组中最大数的下标
        max_index = arr.index(max(arr))
        # 如果最大的数字在头或者尾，返回False
        if max_index == 0 or max_index == len(arr) - 1:
            return False
        # 从max_index向前遍历
        cur_index = max_index
        while cur_index - 1 >= 0:
            if arr[cur_index] <= arr[cur_index - 1]:
                return False
            cur_index -= 1

        # 从max_index向后遍历
        cur_index = max_index
        while cur_index + 1 <= len(arr) - 1:
            if arr[cur_index] <= arr[cur_index + 1]:
                return False
            cur_index += 1

        return True

    def validMountainArray2(self, arr: List[int]) -> bool:
        '''
        func: 遍历一次数组
        假设未发现“山顶”之前，均为升序，若发现后面的数比当前数小，则认为当前为“山顶”，则要求后面的均为降序排列，若后面的发生升序，直接返回false
        param {*}
        return {*}
        '''
        mountain_top_found = False
        mountain_top_times = 0
        mountain_top_index = -1
        # 由于要和后面的元素进行对比，所以只遍历到倒数第二位
        for i in range(len(arr) - 1):
            # 找到山顶，要求后面的数要比当前数小
            # !要考虑相等的情况
            if mountain_top_found:
                if arr[i] <= arr[i + 1]:
                    return False
            # 未找到山顶
            else:
                # 找到山顶位置
                if arr[i] > arr[i + 1]:
                    mountain_top_found = True
                    mountain_top_times += 1
                    mountain_top_index = i
                    if mountain_top_index == 0 or mountain_top_times > 1:
                        return False
                # !要考虑相等的情况
                elif arr[i] == arr[i + 1]:
                    return False
        if mountain_top_found:
            return True
        else:
            return False


if __name__ == "__main__":
    s = Solution()
    print(s.validMountainArray2([4, 4, 3, 2, 1]))
