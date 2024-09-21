# @Time :2024/9/18 9:39
from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = lsum = rsum = 0
        ans = 0

        for right in range(n):
            rsum += 1 - nums[right]
            while lsum < rsum - k:
                lsum += 1 - nums[left]
                left += 1
            ans = max(ans, right - left + 1)

        return ans