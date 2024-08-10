# @Time :2024/9/16 13:48
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = len(nums)
        left = 0  # 左板
        right = k - 1  # 右板
        sum = 0

        for i in range(l - right):
            temp = 0
            for j in range(left, right + 1):
                temp += nums[j]
            if temp < 0:
                sum = temp
            else:
                sum = max(sum, temp)
            left += 1
            right += 1
        return sum / k


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxTotal = total = sum(nums[:k])
        n = len(nums)

        for i in range(k, n):
            total = total - nums[i - k] + nums[i]
            maxTotal = max(maxTotal, total)

        return maxTotal / k


if __name__ == '__main__':
    nums = [-1]
    k = 1
    print(Solution().findMaxAverage(nums, k))
