# @Time :2024/8/17 9:45
from collections import Counter


class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        n = len(word)
        count =  Counter(word[i:i+k] for i in range(0,n,k))
        return n // k - max(count.values())