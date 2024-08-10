# @Time :2024/9/19 9:57
from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)

        res = [[],[]]
        for i in set1:
            if i not in set2:
                res[0].append(i)
        for n in set2:
            if n not in set1:
                res[1].append(n)
        return res
