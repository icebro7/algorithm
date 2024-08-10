# @Time :2024/9/9 8:15

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)

        # 如果其中一个字符串为空，直接返回 0
        if m == 0 or n == 0:
            return 0

        # 使用两个一维数组来优化空间复杂度
        prev = [0] * (n + 1)
        curr = [0] * (n + 1)

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    curr[j] = prev[j - 1] + 1
                else:
                    curr[j] = max(prev[j], curr[j - 1])
            # 交换 prev 和 curr
            prev, curr = curr, prev

        return prev[n]