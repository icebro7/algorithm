from typing import List


class Solution1:
    def removeDuplicates1(self, nums: List[int]) -> int:
        return list(dict.fromkeys(nums))
    #字典法

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        j = 0
        for i in range(n):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]
        return j + 1

    #指针法



if __name__ == '__main__':
    nums = [1,1,2]
    print(Solution().removeDuplicates(nums))