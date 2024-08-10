# @Time :2024/9/12 8:19

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1

        t0 = 0
        t1 = 1
        t2 = 1

        for i in range(3, n + 1):
            next_tribonacci = t0 + t1 + t2
            t0 = t1
            t1 = t2
            t2 = next_tribonacci

        return t2

if __name__ == '__main__':
    n = 25
    print(Solution().tribonacci(n))
