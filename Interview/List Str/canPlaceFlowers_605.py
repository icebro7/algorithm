# @Time :2024/9/14 9:41
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        l = len(flowerbed)
        for i in range(l):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == l - 1 or flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                n -= 1
            if n <= 0:
                return True

        return False


if __name__ == '__main__':
    flowerbed = [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1]

    n = 5
    print(Solution().canPlaceFlowers(flowerbed, n))
