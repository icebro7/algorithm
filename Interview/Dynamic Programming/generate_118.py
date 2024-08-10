# @Time :2024/9/7 9:21

from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows < 3:
            if numRows == 0:
                return []
            if numRows == 1:
                return [[1]]
            if numRows == 2:
                return [[1], [1, 1]]
        res = [[1], [1, 1]]
        for i in range(3, numRows + 1):
            temp = [1] * i
            for j in range(1, i - 1):
                temp[j] = res[i - 2][j - 1] + res[i - 2][j]
            res.append(temp)
        return res


if __name__ == '__main__':
    numRows = 5
    print(Solution().generate(numRows))