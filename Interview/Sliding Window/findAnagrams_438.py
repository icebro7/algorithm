# @Time :2024/9/3 11:06
from typing import List

# 超时
# class Solution:
#     def findAnagrams(self, s: str, p: str) -> List[int]:
#         gap = len(p)
#         fast, slow = gap - 1, 0
#         result = []
#         while fast < len(s):
#             if sorted(s[slow:fast+1]) == sorted(p):
#                 result.append(slow)
#             slow += 1
#             fast += 1
#         return result

from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        p_count = Counter(p)
        window_count = Counter()

        p_len = len(p)

        result = []

        for i in range(len(s)):
            # 将当前字符加入窗口计数器
            window_count[s[i]] += 1
            # 如果窗口大小超过了目标字符串的长度，移除窗口最左边的字符
            if i >= p_len:
                if window_count[s[i - p_len]] == 1:
                    del window_count[s[i - p_len]]
                else:
                    window_count[s[i - p_len]] -= 1
            # 如果窗口计数器与目标字符串计数器相同，记录起始索引
            if window_count == p_count:
                result.append(i - p_len + 1)

        return result



if __name__ == '__main__':
    s = "abab"
    p = "ab"
    print(Solution().findAnagrams(s, p))
