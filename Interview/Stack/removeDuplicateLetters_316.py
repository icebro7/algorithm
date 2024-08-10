# @Time :2024/9/13 14:53
from collections import Counter


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        left = Counter(s)
        stack = []
        in_stack = set()
        for c in s:
            left[c] -= 1
            if c in in_stack:
                continue
            while stack and c < stack[-1] and left[stack[-1]]:
                in_stack.remove(stack.pop())
            stack.append(c)
            in_stack.add(c)
        return ''.join(stack)
