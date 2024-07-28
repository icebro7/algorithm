from typing import List
import time


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # L = len(nums)       # 要跳到的最后位置
        # temp = 0
        #
        #
        # start = nums[0]     # 获取第一个数作为跳跃的跳板，即可以跳跃的数
        # for index, value in enumerate(List[:start],start=1):        # 从第二位到跳跃的数中，获取可以跳到最后一位的元素
        # # 使用for循环来获取索引
        #     temp = max(temp,index + value)
        #     if temp >= L - 1:
        #         return True
        # return False

        n, rightmost = len(nums), 0
        for i in range(n):    #使用for循环来获取索引
            if i <= rightmost:
                rightmost = max(rightmost, i + nums[i])
                if rightmost >= n - 1:
                    return True
        return False

        # 到达最后一个下标


if __name__ == '__main__':
    s_time = time.time()
    nums = [4, 0, 0, 0, 0]
    print(Solution().canJump(nums))
    e_time = time.time()
    a_time = e_time - s_time
    print(a_time)