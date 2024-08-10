# @Time :2024/9/7 7:58
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in range(len(nums)):
            for j in range(len(res)):
                res.append(res[j] + [nums[i]])
        return res

if __name__ == '__main__':
    nums = [1,2,3]
    print(Solution().subsets(nums))