# class Solution(object):
#     def maxArea(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """
#
#         length = len(height)    #首先记录整串数字的长度
#         max_num = max(height)    #获取整个容器中最长的那块木板
#         indices = [i for i, x in enumerate(height) if x == max_num] #将那块木板的索引记录下来，有可能是多块
#         area = [0]  #初始值
#         for i in range(length):
#             for x in indices:    #依次计算每块最长木板与其他木板的最大面积
#                 temp_area = height[i] * abs(x - i)  #获取从第i位计算与墙壁之间的面积
#                 if temp_area > area[0]:
#                     area[0] = temp_area
#         return area[0]
#
#     # 两条短边也有可能构成最大面积

class Solution(object):
    def maxArea(self, height):
        l, r = 0, len(height) - 1   #从数据两边开始做起移动
        ans = 0
        while l < r:    #如果左边的指针一直都小于右边，则正常继续循环
            area = min(height[l], height[r]) * (r - l)  # 记录下面积，最短的那条边乘以两条边之间的距离
            ans = max(ans, area)    # 将当前ans（暂时储存区）与现在计算出来的值做对比，更大的那个进入暂时存储区
            if height[l] <= height[r]:  #指针做移动，以墙壁的高低作为条件，最短的那条墙壁做移动
                l += 1
            else:
                r -= 1
        return area

# 双指针法，从两端分别计算最大的面积，从最小的那一侧开始做指针移动


