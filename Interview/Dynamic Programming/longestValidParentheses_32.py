# @Time :2024/9/9 8:31

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n == 0: return 0

        dp = [0] * n
        res = 0

        for i in range(1, n):
            if s[i] == ")":
                if s[i - 1] == "(":
                    dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
                elif i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == "(":
                    dp[i] = dp[i - 1] + (dp[i - dp[i - 1] - 2] if i - dp[i - 1] >= 2 else 0) + 2

                res = max(res, dp[i])

        return res