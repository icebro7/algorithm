# @Time :2024/9/21 7:57

class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for i in s:
            if i == '*':
                stack.pop()
            else:
                stack.append(i)
        return ''.join(stack)

if __name__ == '__main__':
    s = "leet**cod*e"
    print(Solution().removeStars(s))