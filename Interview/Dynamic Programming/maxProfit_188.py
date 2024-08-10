# @Time :2024/8/9 10:19
from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        k = min(k, n // 2)
        buy_profit = [[0] * (k + 1) for _ in range(n)]
        sell_profit = [[0] * (k + 1) for _ in range(n)]

        buy_profit[0][0], sell_profit[0][0] = -prices[0], 0
        for i in range(1, k + 1):
            buy_profit[0][i] = sell_profit[0][i] = float("-inf")

        for i in range(1, n):
            buy_profit[i][0] = max(buy_profit[i - 1][0], sell_profit[i - 1][0] - prices[i])
            for j in range(1, k + 1):
                buy_profit[i][j] = max(buy_profit[i - 1][j], sell_profit[i - 1][j] - prices[i])
                sell_profit[i][j] = max(sell_profit[i - 1][j], buy_profit[i - 1][j - 1] + prices[i])

        return max(sell_profit[n - 1])