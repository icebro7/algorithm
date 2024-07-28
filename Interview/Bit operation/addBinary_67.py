# @Time :2024/7/19 9:38
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return '{0:b}'.format(int(a,2) + int(b,2))      # 直接转化


if __name__ == '__main__':
    a = "11"
    b = "1"
    print(Solution().addBinary(a,b))