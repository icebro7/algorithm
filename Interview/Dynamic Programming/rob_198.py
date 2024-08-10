# @Time :2024/8/3 8:57
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # numsum = 0
        # n = len(nums)
        # if n < 3:
        #     numsum = max(nums)
        #
        # # 从第三位开始，可以选择由第一位或第二位开始检索

        if not nums:
            return 0
        size = len(nums)

        if size == 1:
            return nums[0]

        first,second = nums[0],max(nums[0],nums[1])

        for i in range(2,size):
            first,second = second,max(first + nums[i],second)


        return second


if __name__ == '__main__':
    nums = [1,2,3,4,5,6,7,8,9,10]
    print(Solution().rob(nums))