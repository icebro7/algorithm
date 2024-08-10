# @Time :2024/9/18 10:06
from itertools import accumulate
from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s = sum(nums)
        for i, (num, pre) in enumerate(zip(nums, accumulate(nums, initial=0))):
            if pre * 2 == s - num:
                return i
        return -1
