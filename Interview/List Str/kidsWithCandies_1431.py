# @Time :2024/9/14 9:29
from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        l = len(candies)
        max_candy = max(candies)
        res = []
        for i in range(l):
            if candies[i] + extraCandies >= max_candy:
                res.append(True)
            else:
                res.append(False)
        return res