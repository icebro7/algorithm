# @Time :2024/9/12 7:50
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l = len(nums)
        left = 1
        right = l - 1
        while left < right:
            mid = int((left + right) / 2)
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
            if count > mid:
                right = mid
            else:
                left = mid + 1
        return left