# @Time :2024/7/31 11:00
from functools import reduce
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)