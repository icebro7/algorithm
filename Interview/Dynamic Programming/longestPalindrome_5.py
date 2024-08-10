# @Time :2024/8/6 10:02

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        result = ''

        for i in range(n-1, -1, -1):
            for j in range(i,n):
                if s[i] == s[j] and (j - i <= 1 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    if j - i + 1 > len(result):
                        result = s[i:j + 1]

        return result