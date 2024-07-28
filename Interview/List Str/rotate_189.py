from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        L = len(nums)
        n = -1
        temp = []

        if L == 0:
            return  nums

        for x in range(L - k):
            temp.append(nums[x])  #先将前x个的数据放入temp列表

        for i in range(k):
            temp.insert(0,nums[n - i])

        for y in range(L):
            nums[y] = temp[y]

# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         if k := (k % len(nums)):
#             nums[:k], nums[k:] = nums[-k:], nums[:-k]


if __name__ == '__main__':
    nums = [-1,0]
    k = 2
    print(Solution().rotate(nums,k))


