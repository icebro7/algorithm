# @Time :2024/8/14 9:29
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        result,path = [],[]
        def dfs(i):
            if i == l:
                result.append(path[:])
                return
            for j in range(0,l):
                if nums[j] not in path:
                    path.append(nums[j])
                    dfs(i + 1)
                    path.pop()
        dfs(0)
        return result








if __name__ == '__main__':

    nums = [1,2,3]
    print(Solution().permute(nums))