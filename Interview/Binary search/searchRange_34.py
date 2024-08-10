# @Time :2024/8/10 10:17
from typing import List

def lower_bound2(nums: List[int], target: int) -> int:
    start, end = 0, len(nums)
    while start < end:
        mid = start + (end - start) // 2
        if nums[mid] < target:
            start = mid + 1
        else:
            end = mid

    return start


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start_index = lower_bound2(nums, target)
        if start_index == len(nums) or nums[start_index] != target:
            return [-1, -1]
        end_index = lower_bound2(nums, target + 1) - 1
        return [start_index, end_index]