import time
from typing import List


# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         L = len(strs)
#         ele_len = len(max(strs, key=len))
#         mark = 0
#         temp = ""
#
#
#
#         if L == 0 :
#             return ""
#
#         for i in range(ele_len):
#             temp.join(strs[0][mark])
#             if temp == strs[i]

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""
        str0 = min(strs)
        str1 = max(strs)
        for i in range(len(str0)):
            if str0[i] != str1[i]:
                return str0[:i]
        return str0





if __name__ == '__main__':

    s_time = time.time()
    strs = ["fl", "flxxxxw", "flight"]
    print(Solution().longestCommonPrefix(strs))
    e_time = time.time()
    a_time = e_time - s_time
    print(a_time)

