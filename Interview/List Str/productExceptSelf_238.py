import time
from typing import List


# class Solution:
# def productExceptSelf(self, nums: List[int]) -> List[int]:
#     L = len(nums)
#     answer = [1] * L
#     for i in range(L):
#         for x in range(L):
#             if x == i:
#                 continue
#             answer[i] = answer[i] * nums[x]
#
#     return answer
# 两个for循环超出时间限制，时间复杂度O（n^2）

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        L = len(nums)
        left_products = [1] * L
        right_products = [1] * L
        answer = [1] * L
        # 计算每个位置左侧所有元素的乘积
        for i in range(1, L):
            left_products[i] = left_products[i - 1] * nums[i - 1]
        # 计算每个位置右侧所有元素的乘积
        for i in range(L - 2, -1, -1):
            right_products[i] = right_products[i + 1] * nums[i + 1]

        # 将左右乘积相乘得到最终结果
        for i in range(L):
            answer[i] = left_products[i] * right_products[i]

        return answer


if __name__ == '__main__':
    s_time = time.time()
    nums = [1, 2, 3, 4]
    print(Solution().productExceptSelf(nums))
    e_time = time.time()
    a_time = e_time - s_time
    print(a_time)
