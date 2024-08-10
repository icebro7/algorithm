# @Time :2024/8/10 9:50
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        maxn = 0
        for i in range(1,len(nums)):
            if nums[i] > nums[maxn]:
                maxn = i
        return maxn