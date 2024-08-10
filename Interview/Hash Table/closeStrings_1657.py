# @Time :2024/9/19 10:20
from collections import Counter


class Solution:
    def closeStrings(self, s: str, t: str) -> bool:
        return set(s) == set(t) and Counter(Counter(s).values()) == Counter(Counter(t).values())
