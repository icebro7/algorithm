# @Time :2024/9/4 7:59
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre, maxAns = 0, nums[0]
        for x in nums:
            pre = max(pre + x, x)
            maxAns = max(maxAns, pre)
        return maxAns

if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(Solution().maxSubArray(nums))