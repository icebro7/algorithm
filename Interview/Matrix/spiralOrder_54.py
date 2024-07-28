from typing import List

# class Solution:
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#         if not matrix or not matrix[0]:
#             return []
#
#         m, n = len(matrix), len(matrix[0])
#         top, bottom, left, right = 0, m - 1, 0, n - 1
#         ans = []
#
#         while top <= bottom and left <= right:
#             # 横向从左至右
#             for i in range(left, right + 1):
#                 ans.append(matrix[top][i])
#             top += 1
#
#             # 竖向从上至下
#             for i in range(top, bottom + 1):
#                 ans.append(matrix[i][right])
#             right -= 1
#
#             if top > bottom or left > right:
#                 break
#
#             # 横向从右至左
#             for i in range(right, left - 1, -1):
#                 ans.append(matrix[bottom][i])
#             bottom -= 1
#
#             # 竖向从下至上
#             for i in range(bottom, top - 1, -1):
#                 ans.append(matrix[i][left])
#             left += 1
#
#         return ans

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        l, t = 0, 0
        r, b = len(matrix[0]) - 1, len(matrix) - 1
        ans = []
        while l <= r and t <= b:
            for i in range(l, r + 1):
                ans.append(matrix[t][i])

            for i in range(t + 1, b + 1):
                ans.append(matrix[i][r])
            if l < r and t < b:
                for i in range(r - 1, l, -1):
                    ans.append(matrix[b][i])
                for i in range(b, t, -1):
                    ans.append(matrix[i][l])
            l += 1
            t += 1
            r -= 1
            b -= 1
        return ans

# 测试代码
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(Solution().spiralOrder(matrix))
