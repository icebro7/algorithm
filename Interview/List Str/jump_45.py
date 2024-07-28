from typing import List
import time

# class Solution:
#     def jump(self, nums: List[int]) -> int:
#         L = len(nums)
#         arrive = 0
#         for i in range(L):      # 总共循环的次数
#             if i <= arrive:     #界定位，该此循环只能至多到达这个位置
#                 arrive = max(arrive,i + nums[i])        # 循环判断是否能够到达最后一位
#
#                 if arrive >= L -  1:
#                     return True

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        maxPos, end, step = 0, 0, 0
        for i in range(n - 1):
            if maxPos >= i:
                maxPos = max(maxPos, i + nums[i])
                if i == end:
                    end = maxPos
                    step += 1
        return step


if __name__ == '__main__':
    s_time = time.time()
    nums = [1, 1, 1, 1, 0]
    print(Solution().jump(nums))
    e_time = time.time()
    a_time = e_time - s_time
    print(a_time)