from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows_to_zero = set()
        cols_to_zero = set()
        # 第一次遍历，找到所有0的行和列
        for row_index, row in enumerate(matrix):
            for col_index, value in enumerate(row):
                if value == 0:
                    rows_to_zero.add(row_index)
                    cols_to_zero.add(col_index)

        # 第二次遍历，根据记录的行和列索引，将对应行和列置为0
        for row in rows_to_zero:
            for col_index in range(len(matrix[0])):
                matrix[row][col_index] = 0

        for col in cols_to_zero:
            for row_index in range(len(matrix)):
                matrix[row_index][col] = 0


if __name__ == '__main__':
    matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    Solution().setZeroes(matrix)
    for row in matrix:
        print(row)
