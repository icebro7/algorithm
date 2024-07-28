from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:    #判断是否为空，为空的话直接返回0
            return 0

        n = len(nums)   #获取list的长度
        ans = n + 1     #子数列的最小长度
        start, end = 0, 0      #初始化两个滑动窗口
        total = 0       #两个滑动窗口之间数的和
        while end < n:      #下方的滑动窗口不能超过list的长度，相等时说明到头了
            total += nums[end]      #总数等于下方滑块的数
            while total >= s:       #当总数比目标数更大时执行循环，否则把下方的滑块往后移动一位
                ans = min(ans, end - start + 1)     #把循环中子序列最小的长度保存再ans中
                total -= nums[start]    #总数减去上方滑块的值，并且将上方滑块的索引往后移动一位
                start += 1
            end += 1

        #整个列表都会全部循环，寻找出最短的子序列

        return 0 if ans == n + 1 else ans

if __name__ == '__main__':
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    print(Solution().minSubArrayLen(target,nums))

