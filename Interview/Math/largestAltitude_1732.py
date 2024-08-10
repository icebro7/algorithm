# @Time :2024/9/18 9:56
from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        start = 0
        heal = float('-inf')
        for i in range(len(gain)):
            start += gain[i]
            heal = max(start,heal)
        if heal < 0:
            return 0

        return heal


if __name__ == '__main__':
    gain = [-4,-3,-2,-1,4,3,2]
    print(Solution().largestAltitude(gain))