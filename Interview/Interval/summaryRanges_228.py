from typing import List


# class Solution:
    # def summaryRanges(self, nums: List[int]) -> List[str]:
    #     head = 0
    #     tail = 1
    #
    #     result = []
    #     while tail > len(nums):
    #         if nums[head] + 1 == nums[tail]:
    #             tail += 1
    #
    #         elif nums[head] + 1 != nums[tail]:
    #             result.append("head")
    #             head =
    #
    #         else:

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        def f(i: int, j: int) -> str:
            return str(nums[i]) if i == j else f'{nums[i]}->{nums[j]}'

        i = 0
        n = len(nums)
        ans = []
        while i < n:
            j = i
            while j + 1 < n and nums[j + 1] == nums[j] + 1:
                j += 1
            ans.append(f(i, j))
            i = j + 1
        return ans






if __name__ == '__main__':
    nums = [0, 1, 2, 4, 5, 7]
    print(Solution().summaryRanges(nums))
