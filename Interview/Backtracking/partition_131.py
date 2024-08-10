# @Time :2024/9/7 8:14
from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        dp = [[[]]]
        for i in range(1,len(s) + 1):
            dp.append([])
            for j in range(i):
                tmp = s[j:i]
                if tmp == tmp[::-1]:
                    dp[-1].extend(l + [tmp] for l in dp[j])
        return dp[-1]

if __name__ == '__main__':
    s = "aabbc"
    print(Solution().partition(s))

