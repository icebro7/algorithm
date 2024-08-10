# @Time :2024/9/9 7:57

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        f = [1] * n
        for i in range(1,m):
            for j in range(1,n):
                f[j] += f[j - 1]
        return f[n - 1]

if __name__ == '__main__':
    m = 3
    n = 9
    print(Solution().uniquePaths(m,n))