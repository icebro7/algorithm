# @Time :2024/8/6 9:22
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        dp = [float('inf')] * n
        dp[0] = 0
        for i in range(m):
            dp[0] += grid[i][0]
            for j in range(1,n):
                dp[j] = min(dp[j],dp[j - 1]) + grid[i][j]


        return dp[-1]