# @Time :2024/4/25 9:25
from typing import List

# 输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
# 输出：[[1,6],[8,10],[15,18]]
# 解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].


# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         temp = []
#         L = len(intervals)
#         x = 0
#         signal = 0
#         for i in range(L):
#             if signal == 0:
#                 site = 1
#                 x = max(intervals[i][site], x)
#                 signal += 1
#
#             else:
#                 site = 0
#                 if intervals[i][site] <= x:
#                     temp.append([x,intervals[i][1]])
#                 signal -= 1


# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         intervals.sort()
#         ans = [intervals[0]]
#         for s, e in intervals[1:]:
#             if ans[-1][1] < s:
#                 ans.append([s, e])
#             else:
#                 ans[-1][1] = max(ans[-1][1], e)
#         return ans

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = [intervals[0]]
        for i,n in intervals[1:]:       # 跳过第一个元素
            if ans[-1][1] > i:
                ans.append([i,n])
            else:
                ans[-1][1] = max(ans[-1][1],n)
        return ans



if __name__ == '__main__':
    intervals = [[1, 3], [2, 6], [8, 10], [19, 20], [15, 18]]
    print(Solution().merge(intervals))
