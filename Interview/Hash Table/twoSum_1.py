from typing import List


# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         L = len(nums)
#         point_f = 0
#         point_b = L - 1  # 双指针解法，第一个与最后一个
#         new_nums = nums  # 从小到大排序
#         new_nums.sort()
#         temp = []
#         for i in range(L):
#             S = new_nums[point_f] + new_nums[point_b]
#             if S == target:
#                 numb = [point_f,point_b]
#             elif S > target:
#                 point_b -= 1
#             else:
#                 point_f += 1
#
#         for i in nums:
#             if numb[0] == nums[i] or numb[1] == nums[i]:
#                 temp.append(i)
#
#         return temp

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 使用字典来存储每个数字的索引，以便快速查找
        num_dict = {}
        # 遍历数组
        for i, num in enumerate(nums):
            # 计算目标值与当前数字的差
            complement = target - num
            # 检查差值是否存在于字典中
            if complement in num_dict:
                # 如果存在，返回差值的索引和当前索引
                return [num_dict[complement], i]
            num_dict[num] = i


if __name__ == '__main__':
    nums = [3,2,4]
    target = 6
    print(Solution().twoSum(nums, target))

