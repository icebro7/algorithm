# @Time :2024/9/18 9:47
from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        cnt = 0
        ans = 0
        left = 0
        for right, x in enumerate(nums):
            if x == 0:
                cnt += 1
            while cnt > 1:
                if nums[left] == 0:
                    cnt -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans - 1
