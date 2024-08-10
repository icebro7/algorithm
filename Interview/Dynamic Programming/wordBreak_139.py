# @Time :2024/8/3 9:35

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        word = set(wordDict)

        for i in range(n):
            if dp[i]:
                for j in range(i + 1,n + 1):
                    if s[i:j] in word:
                        dp[j] = True

        return dp[n]

if __name__ == '__main__':
    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    print(Solution().wordBreak(s,wordDict))
