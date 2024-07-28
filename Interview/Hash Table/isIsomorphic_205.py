# from collections import Counter
#
# class Solution:
#     def isIsomorphic(self, s: str, t: str) -> bool:
#         if len(set(s)) == len(s):        # 说明并没有规律
#             return False
#         letter_counts_s = Counter(s)
#
#
#         # 筛选出出现次数大于1的字符
#         same_letters_s = {letter: count for letter, count in letter_counts_s.items() if count > 1}
#
#         same_key = list(same_letters_s.keys())
#
#         for i in same_key:
#             site = s.find(i)
#         return same_key


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return all(s.index(s[i]) == t.index(t[i])  for i in range(len(s)))






if __name__ == '__main__':
    s = "aabbccccc"
    t = "bbaaddddd"
    print(Solution().isIsomorphic(s,t))
