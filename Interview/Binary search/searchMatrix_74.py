# @Time :2024/8/10 9:33
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        low, high = 0, m * n - 1
        while low <= high:
            mid = int((high - low) / 2) + low
            x = matrix[int(mid / n)][mid % n]
            if x < target:
                low = mid + 1
            elif x > target:
                high = mid - 1
            else:
                return True

        return False