from typing import List

# j = 1  # 循环位
# mark = 0  # 标记是否有重复的位
#
# for i in range(L):  # 判断每位数
#     if nums[i] == nums[j]:  # 如果前后两个数相等的话
#
#         if mark == 2:
#             nums.remove(nums[j])
#             mark = 0
#     mark += 1
#     j += 1

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        L = len(nums)
        if L < 2:
            return L

        fast,slow = 2,2
        while fast < L:
            if nums[slow - 2] != nums[fast]:      # 判断的是最多两个连续的数
                nums[slow] = nums[fast]           # 把跑的慢的数赋给跑得快的数
                slow += 1                         # 慢的往前走一位

            fast += 1                             # 不管两个数是否相等，都往前跑
        return slow


if __name__ == '__main__':
    nums = [1,1,1,2,2,3]
    print(Solution().removeDuplicates(nums))

