# @Time :2024/9/3 21:54
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum_count = {0:1}
        prefix_sum = 0
        count = 0

        for num in nums:
            prefix_sum += num

            if prefix_sum - k in prefix_sum_count:
                count += prefix_sum_count[prefix_sum - k]
            if prefix_sum in prefix_sum_count:
                prefix_sum_count[prefix_sum] += 1
            else:
                prefix_sum_count[prefix_sum] = 1
        return count