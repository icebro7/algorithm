# @Time :2024/9/14 10:03
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        leftMin = [0] * n
        leftMin[0] = nums[0]
        for i in range(1, n):
            leftMin[i] = min(leftMin[i - 1], nums[i])
        rightMax = [0] * n
        rightMax[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], nums[i])
        for i in range(1, n - 1):
            if leftMin[i - 1] < nums[i] < rightMax[i + 1]:
                return True
        return False
