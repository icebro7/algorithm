import time
from typing import List


# [7,1,4,3,6,4]
# 第二天买入：1   第三天卖出：4     3
# 第四天买入：3   第五天卖出：6     3

# [1,2,3,2,5,6]
# 第一天买入：1   第三天卖出：3     2
# 第四天买入：2   第五天卖出：6     4

# [1,3,7,4,5,6]
# 第一天买入：1   第三天卖出：7     6
# 第四天买入：4   第五天卖出：6     2


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        ans = 0
        L = len(prices)

        for i in range(1,L):
            if prices[i] > prices[i - 1]:
                ans += (prices[i] - prices[i - 1]);

        return ans


if __name__ == '__main__':
    s_time = time.time()
    prices = [7,1,3,4,6,4]
    print(Solution().maxProfit(prices))
    e_time = time.time()
    a_time = e_time - s_time
    print(a_time)
