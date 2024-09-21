# @Time :2024/8/5 10:17
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        f = [0] * n
        f[0] = triangle[0][0]
        for i in range(1,n):
            f[i] = f[i - 1] + triangle[i][i]
            for j in range(i - 1,0,-1):
                f[j] = min(f[j - 1],f[j]) + triangle[i][j]
            f[0] += triangle[i][0]

        return min(f)