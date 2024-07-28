from typing import List


# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         max_conse = 0
#         count = []
#         makr = 0
#         sort_nums = sorted(nums)
#         if len(nums) <= 1:
#             return len(nums)
#
#         for i in sort_nums:
#             makr = i - makr
#             if makr == 1:

# class Solution(object):
#     def longestConsecutive(self, nums):
#         hash_dict = dict()
#
#         max_length = 0
#         for num in nums:
#             if num not in hash_dict:
#                 left = hash_dict.get(num - 1, 0)
#                 right = hash_dict.get(num + 1, 0)
#
#                 cur_length = 1 + left + right
#                 if cur_length > max_length:
#                     max_length = cur_length
#
#                 hash_dict[num] = cur_length
#                 hash_dict[num - left] = cur_length
#                 hash_dict[num + right] = cur_length
#
#         return max_length

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0  # 记录最长连续序列的长度
        num_set = set(nums)  # 记录nums中的所有数值
        for num in num_set:
            # 如果当前的数是一个连续序列的起点，统计这个连续序列的长度
            if (num - 1) not in num_set:
                seq_len = 1  # 连续序列的长度，初始为1
                while (num + 1) in num_set:
                    seq_len += 1
                    num += 1  # 不断查找连续序列，直到num的下一个数不存在于数组中
                res = max(res, seq_len)  # 更新最长连续序列长度
        return res


if __name__ == '__main__':
    nums = [100, 4, 200, 1, 3, 2]
    print(Solution().longestConsecutive(nums))
