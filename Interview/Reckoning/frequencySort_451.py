# @Time :2024/9/2 11:23
from collections import Counter
import heapq

class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        sorted_items = heapq.nlargest(len(s), count.items(), key=lambda item: item[1])
        res = ''.join(char * freq for char, freq in sorted_items)

        return res
