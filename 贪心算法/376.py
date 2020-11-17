'''
Descripttion: 376 摆动序列
version: 1
Author: Jason
Date: 2020-11-16 22:09:31
LastEditors: Jason
LastEditTime: 2020-11-17 14:10:58
'''


from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]):
        '''
        func: 动作机，拐点即为保留的数字
        param {*}
        return {*}
        '''
        begin = 0
        up = 0
        down = 0

        length = len(nums)
        if length < 2:
            return length

        res = 1
        diff = nums[1] - nums[0]
        if diff > 0:
            up = 1
            down = 0
            begin = 0
            res += 1
        elif diff == 0:
            begin = 1
            up = 0
            down = 0
        else:
            down = 1
            begin = 0
            up = 0
            res += 1

        for i in range(2, length):
            diff = nums[i] - nums[i - 1]
            # 之前处于上升过程
            if up:
                # 如果还是上升
                if diff >= 0:
                    continue
                else:
                    down = 1
                    up = 0
                    res += 1

            # 之前处于下降过程
            elif down:
                # 如果还是下降
                if diff <= 0:
                    continue
                else:
                    up = 1
                    down = 0
                    res += 1

            # 之前处于启动过程
            else:
                # 如果处于上升状态
                if diff > 0:
                    up = 1
                    begin = 0
                    res += 1
                # 如果还是开始状态
                elif diff == 0:
                    continue
                # 如果处于下降状态
                else:
                    down = 1
                    begin = 0
                    res += 1
        return res

    def wiggleMaxLength2(self, nums: List[int]):
        begin = 1
        up = 0
        down = 0
        length = len(nums)
        if length < 2:
            return length
        res = 1
        for i in range(1, length):
            diff = nums[i] - nums[i - 1]
            # 如果之前处于begin状态
            if begin:
                if diff > 0:
                    up = 1
                    begin = 0
                    res += 1
                elif diff < 0:
                    down = 1
                    begin = 0
                    res += 1
                # 如果相等，继续begin
                else:
                    continue

            # 如果之前处于up状态
            elif up:
                if diff < 0:
                    down = 1
                    up = 0
                    res += 1

            # 如果之前处于down状态
            else:
                if diff > 0:
                    up = 1
                    down = 0
                    res += 1
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.wiggleMaxLength2([0, 0]))
