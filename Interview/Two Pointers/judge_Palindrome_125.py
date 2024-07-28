# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         # 将str处理干净，消除所有的非字母数字字符
#         s = ''.join(char for char in s if char.isalnum())
#         s = s.lower()  # 将字符串转换为小写
#
#
#         return s == s[::-1]

        # 翻转法

class Solution:
    def isPalindrome(self, s: str) -> bool:
        sgood = "".join(ch.lower() for ch in s if ch.isalnum())

        n = len(sgood)
        left, right = 0, n - 1

        while left < right:
            if sgood[left] != sgood[right]:
                return False
            left, right = left + 1, right - 1
        return True




if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"
    print(Solution().isPalindrome(s))
