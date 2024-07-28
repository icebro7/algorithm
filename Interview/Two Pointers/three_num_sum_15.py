# class Solution(object):
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         #每个元素都不能被重复使用，并且元素相加为0
#         l, r = 0, len(nums) - 1  # 从数据两边开始做起移动
#         temp = []   #暂时存储区
#
#
#         for i in range(len(nums)):  #从第一个开始做起循环，后续默认跳过i开始移动指针
#             while l < r:
#                 if l == i:
#                     l += 1
#                     continue
#                 else:
#                     # 首位已经确定，后续只要与跳过首位的两个索引进行相加
#                     s = nums[i] + nums[l] +nums[r]
#                     if s == 0:  #如果符合相加为0的话，记录索引
#                         temp.append([i,l,r])
#                     if nums[l] + nums[i] >= nums[r] + nums[i]:
#                         l += 1
#                     else:
#                         r -= 1
#
#         return temp
#


class Solution:
    def threeSum(self, nums):

        n = len(nums)
        if not nums or n < 3:
            return []
        nums.sort() #做从小到的的排序
        res = []
        for i in range(n):
            if nums[i] > 0:   #若排序后第一个数就大于零的话，那么相加也不可能为0
                return res
            if i > 0 and nums[i] == nums[i - 1]:  #从第二位开始，前一位等于后一位的话，跳过这次循环，默认不满足条件
                continue
            L = i + 1   #跳过第一个指针的第二个指针
            R = n - 1   #从尾部开始的第三个指针
            while (L < R):
                if nums[i] + nums[L] + nums[R] == 0:
                    res.append([nums[i], nums[L], nums[R]])
                    while L < R and nums[L] == nums[L + 1]:
                        L = L + 1
                    while L < R and nums[R] == nums[R - 1]:
                        R = R - 1
                    L = L + 1
                    R = R - 1
                elif nums[i] + nums[L] + nums[R] > 0: #如果大于0的话，说明尾部过大，第三个指针移动
                    R = R - 1
                else:
                    L = L + 1
        return res
# if __name__ == '__main__':
#     num = [-1,0,1,2,-1,-4]
#     print(Solution().threeSum(num))









