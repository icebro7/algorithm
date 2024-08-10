# @Time :2024/7/31 10:38
class Solution:
    def hammingWeight(self, n: int) -> int:
        ret = 0
        while n:
            n &= n -1
            ret += 1
        return ret