# @Time :2024/9/2 9:51
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        L = len(nums)
        M = L / 3
        result = []
        element_count = {}
        for element in nums:
            if element in element_count:
                element_count[element] += 1
            else:
                element_count[element] = 1
        for key,value in element_count.items():
            if value > M:
                result.append(key)
        return result

if __name__ == '__main__':
    nums = [3, 2, 3]
    print(Solution().majorityElement(nums))

