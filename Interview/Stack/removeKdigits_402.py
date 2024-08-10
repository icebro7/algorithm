# @Time :2024/9/13 14:26

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        remain = len(num) - k
        for digit in num:
            while k and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        return ''.join(stack[:remain]).lstrip('0') or '0'

if __name__ == '__main__':
    num = "1032219"
    k = 3
    print(Solution().removeKdigits(num, k))