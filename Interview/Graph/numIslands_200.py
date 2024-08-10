# @Time :2024/9/6 8:04

class Solution:
    def numIslands(self, grid: [[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == '0':
                return
            grid[i][j] = '0'
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1

        return count


if __name__ == '__main__':
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "1", "0"]
    ]
    print(Solution().numIslands(grid))
