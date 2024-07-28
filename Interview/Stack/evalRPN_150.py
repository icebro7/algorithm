# @Time :2024/7/11 9:06
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = list()
        sign = ['+', '-', '*', '/']

        for elm in tokens:
            if elm in sign:
                b = stack.pop()
                a = stack.pop()

                if elm == "+":
                    stack.append(a + b)
                elif elm == "-":
                    stack.append(a - b)
                elif elm == "*":
                    stack.append(a * b)
                elif elm == "/":
                    stack.append(int(a / b))

            else:
                stack.append(int(elm))

        return stack[0]


if __name__ == '__main__':
    tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    print(Solution().evalRPN(tokens))