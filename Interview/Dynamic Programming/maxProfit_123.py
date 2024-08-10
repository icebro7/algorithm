# @Time :2024/8/9 9:50
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 1:
            return 0
        first_buy = second_buy = -prices[0]
        first_sell = second_sell = 0

        for price in prices[1:]:
            first_buy = max(first_buy,-price)
            first_sell = max(first_sell,first_buy + price)
            second_buy = max(second_buy,first_sell - price)
            second_sell = max(second_sell,second_buy + price)

        return second_sell