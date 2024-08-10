# @Time :2024/8/3 10:11
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coin in sorted(coins):
            for x in range(coin,amount + 1):
                dp[x] = min(dp[x],dp[x - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1
