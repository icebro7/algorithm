# @Time :2024/9/2 14:57
from typing import List
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        max_freq = max(freq.values())
        max_freq_count = sum(1 for v in freq.values() if v == max_freq)

        part_count = max_freq - 1
        part_length = n - (max_freq_count - 1)
        empty_slots = part_count * part_length
        available_tasks = len(tasks) - max_freq * max_freq_count
        idles = max(0, empty_slots - available_tasks)

        return len(tasks) + idles
