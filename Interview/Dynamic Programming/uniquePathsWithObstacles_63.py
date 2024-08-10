# @Time :2024/8/6 9:45
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        height, width = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        dp = [[0] * width for _ in range(height)]
        dp[0][0] = 1
        for m in range(height):
            for i in range(width):
                if obstacleGrid[m][i] == 0:
                    if m > 0:
                        dp[m][i] += dp[m - 1][i]

                    if i > 0:
                        dp[m][i] += dp[m][i - 1]

        return dp[-1][-1]
