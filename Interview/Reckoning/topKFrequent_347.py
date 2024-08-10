# @Time :2024/9/2 11:02
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        L = len(nums)
        element_count = {}

        for element in nums:
            if element in element_count:
                element_count[element] += 1
            else:
                element_count[element] = 1
        sorted_items = sorted(element_count.items(), key=lambda item: item[1], reverse=True)
        top_x_keys = [item[0] for item in sorted_items[:k]]
        return top_x_keys

if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    k = 6
    print(Solution().topKFrequent(nums, k))