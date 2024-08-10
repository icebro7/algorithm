# @Time :2024/8/2 9:37

class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n > 0:
            n //= 5
            count += n
        return count

if __name__ == '__main__':
    n = 1010
    print(Solution().trailingZeroes(n))


