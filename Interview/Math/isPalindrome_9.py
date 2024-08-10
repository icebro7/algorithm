# @Time :2024/8/2 9:11

class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        re = str_x[::-1]

        return str_x == re

if __name__ == '__main__':
    x = 121
    print(Solution().isPalindrome(x))

