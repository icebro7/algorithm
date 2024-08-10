# @Time :2024/9/7 8:58
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.res = []
        cur = [['.' for _ in range(n)] for _ in range(n)]
        self.backtracking(cur, 0, n)
        return self.res

    def backtracking(self, cur: List[List[str]], level: int, n: int):
        if level == n:
            self.res.append([''.join(row) for row in cur])
            return
        for j in range(n):
            if self.isValid(cur, level, j):
                cur[level][j] = 'Q'
                self.backtracking(cur, level + 1, n)
                cur[level][j] = '.'

    def isValid(self, cur: List[List[str]], i: int, j: int) -> bool:
        n = len(cur)
        for a in range(n):
            if cur[a][j] == 'Q':
                return False
        a,b = i,j
        while a >= 0 and b >= 0:
            if cur[a][b] == 'Q':
                return False
            a -= 1
            b -= 1
        a,b = i,j
        while a >= 0 and b < n:
            if cur[a][b] == 'Q':
                return False
            a -= 1
            b += 1
        return True

if __name__ == '__main__':
    n = 8
    print(Solution().solveNQueens(n))
