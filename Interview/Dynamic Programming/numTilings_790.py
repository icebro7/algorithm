# @Time :2024/9/21 10:29

MOD = 10 ** 9 + 7

class Solution:
    def numTilings(self, n: int) -> int:
        if n == 1: return 1
        a, b, c = 1, 1, 2
        for _ in range(3, n + 1):
            a, b, c = b, c, (c * 2 + a) % MOD
        return c
