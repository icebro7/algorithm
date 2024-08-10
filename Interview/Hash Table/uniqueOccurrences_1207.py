# @Time :2024/9/19 10:08
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashmap1 = {i: 0 for i in arr}
        hashmap2 = {}
        for i in arr:
            hashmap1[i] += 1
        for i in hashmap1.keys():
            hashmap2[hashmap1[i]] = i

        return len(hashmap1.keys()) == len(hashmap2.keys())
