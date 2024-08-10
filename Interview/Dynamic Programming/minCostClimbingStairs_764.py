# @Time :2024/9/21 10:15
from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        pre = curr = 0
        for i in range(2,n + 1):
            next = min(curr + cost[i - 1], pre + cost[i - 2])
            pre, curr = curr, next
        return curr

