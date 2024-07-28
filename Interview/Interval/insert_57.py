# @Time :2024/4/29 8:08
from typing import List

# 输入：intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# 输出：[[1,2],[3,10],[12,16]]
# 解释：这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # start, end = newInterval
        # ans = [intervals[0]]
        # for i,n in intervals[1:]:
        #     if start > ans[-1][1]:      # 如果另一个区间的数在intervals的元素中
        #         ans.append([i,n])
        #
        #     else:
        #
        #
        #     print(i,n)
        # print(ans)

        # merged = []
        # i = 0
        # n = len(intervals)
        #
        # # 找到所有与 newInterval 不重叠且在其左侧的区间，将它们加入 merged 中
        # while i < n and intervals[i][1] < newInterval[0]:
        #     merged.append(intervals[i])
        #     i += 1
        #
        # # 合并与 newInterval 重叠的区间
        # while i < n and intervals[i][0] <= newInterval[1]:
        #     newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
        #     i += 1
        #
        # # 将新合并的区间加入 merged 中
        # merged.append(newInterval)
        #
        # # 将剩余的区间加入 merged 中
        # merged.extend(intervals[i:])
        #
        # return merged


        intervals.append(newInterval)
        intervals.sort()
        ans = []
        temp = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] > temp[1]:
                ans.append(temp)
                temp = intervals[i]
            else:
                temp[1] = max(intervals[i][1], temp[1])
        ans.append(temp)
        return ans


if __name__ == '__main__':
    intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    newInterval = [4, 8]
    Solution().insert(intervals, newInterval)

