from typing import List
from collections import Counter


class Solution:
    # def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    #     nums_count = Counter(nums).most_common(2)  # 所有元素出现的次数
    #     temp_list = []
    #     for i in range(len(nums_count)):        # 筛选出所有出现次数大于2次的元素
    #         if nums_count[i][1] >= 2:
    #             temp_list.append(nums_count.)
    #
    #     for count,value in enumerate(nums):
    #         if value in temp_list:
    #             pass
    #     return False
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        pos = {}
        for i, num in enumerate(nums):
            if num in pos and i - pos[num] <= k:        # 判断该数是否已在字典中，并且绝对值
                return True
            pos[num] = i                                # 如果在判断中不存在，那么把他放进字典中
        return False



if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    k = 3
    print(Solution().containsNearbyDuplicate(nums, k))
    # nums_count = Counter(nums).most_common()  # 所有元素出现的次数

