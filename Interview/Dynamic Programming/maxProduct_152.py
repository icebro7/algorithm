# @Time :2024/9/8 8:56
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = nums[0]
        pre_max = nums[0]
        pre_min = nums[0]
        for num in nums[1:]:
            temp_max = pre_max * num
            temp_min = pre_min * num
            pre_max = max(temp_max, temp_min, num)
            pre_min = min(temp_max, temp_min, num)
            res = max(res, pre_max)
        return res
if __name__ == '__main__':
    nums = [0,-1,-2,-3]
    print(Solution().maxProduct(nums))
