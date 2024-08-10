# @Time :2024/9/11 8:53
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while nums[i] >= nums[j]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        left, right = i + 1, len(nums) - 1
        for k in range((right - left + 1) // 2):
            nums[left + k], nums[right - k] = nums[right - k], nums[left + k]

if __name__ == '__main__':
    nums = [1, 2, 3]
    print(Solution().nextPermutation(nums))
    print(nums)