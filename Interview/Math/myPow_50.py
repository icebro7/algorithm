# @Time :2024/8/2 10:15

class Solution:
    def myPow(self, x: float, n: int) -> float:
        # if x == 0:
        #     return 0.0000
        # sum = 1
        # for _ in range(n):
        #     sum *= x
        #
        # return round(sum,4)

        if x == 0.0:
            return 0.0
        result = 1.0

        if n < 0:
            x = 1 / x
            n = - n

        while n > 0:
            if n & 1:
                result *= x
            x *= x
            n >>= 1

        return result


if __name__ == '__main__':
    x = 2.00000
    n = 10
    print(Solution().myPow(x, n))
