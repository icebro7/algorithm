# @Time :2024/9/3 10:26
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow, fast = 0, 0
        while fast < len(nums):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
            fast += 1
        return nums
if __name__ == '__main__':
    nums = [0,1,0,3,12]
    print(Solution().moveZeroes(nums))
