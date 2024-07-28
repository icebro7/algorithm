# @Time :2024/7/11 10:10
class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')

        res = 0  # 当前结果
        num = 0  # 当前待处理数字
        sign = 1  # 当前符号
        stack = []
        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch == '+':
                res += sign * num
                num = 0
                sign = 1
            elif ch == '-':
                res += sign * num
                num = 0
                sign = -1
            elif ch == '(':
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif ch == ')':
                oldsign = stack.pop()
                oldres = stack.pop()
                res += sign * num
                num = 0
                res *= oldsign
                res += oldres

        res += sign * num
        return res
