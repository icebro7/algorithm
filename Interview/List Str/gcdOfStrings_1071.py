# @Time :2024/9/14 9:18
import math



class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        candidate_len = math.gcd(len(str1), len(str2))
        candidate = str1[: candidate_len]
        if str1 + str2 == str2 + str1:
            return candidate
        return ''





if __name__ == '__main__':
    str1 = "ABCABC"
    str2 = "ABC"
    print(Solution().gcdOfStrings(str1, str2))