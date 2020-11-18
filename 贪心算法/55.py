'''
Descripttion: 跳跃游戏
version: 1
Author: Jason
Date: 2020-11-17 22:11:14
LastEditors: Jason
LastEditTime: 2020-11-18 09:10:49
'''


from typing import List


class Solution:
    def canJump(self, nums: List[int]):
        '''
        func: 判断你是否能够到达最后一个位置。
        max_index是到当前位置为止，所能到达的最远的下标
        current_index是当前下标
        param {*}
        return {*}
        '''
        length = len(nums)
        current_index = 0
        max_index = nums[current_index]
        # 如果当前index未到达末尾（current_index < length），且能从前面的位置跳到当前位置（max_index >= current_index），继续循环
        while current_index < length and max_index >= current_index:
            # 如果当前位置所能到达的最远位置大于之前所能到达的最远位置，则更新最远位置
            if current_index + nums[current_index] >= max_index:
                max_index = current_index + nums[current_index]
            # 如果更新后的最远位置能够到达最后一个位置，停止比较，返回True
            if max_index >= length - 1:
                return True
            current_index += 1
        return False


if __name__ == "__main__":
    s = Solution()
    print(s.canJump([2, 3, 1, 1, 4]))
