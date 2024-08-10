# @Time :2024/9/11 8:33
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        if l == 0:
            return []
        p0 = p1 = 0

        for i in range(l):
            if nums[i] == 1:
                nums[i], nums[p1] = nums[p1], nums[i]
                p1 += 1
            elif nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                if p0 < p1:
                    nums[i], nums[p1] = nums[p1], nums[i]
                p0 += 1
                p1 += 1

if __name__ == '__main__':
    nums = [2,0,2,1,1,0]
    print(Solution().sortColors(nums))
    print(nums)




