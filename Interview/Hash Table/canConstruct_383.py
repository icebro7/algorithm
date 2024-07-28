# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         L_son = len(magazine)
#         L_pr = len(ransomNote)
#         for i in range(L_pr):                        # 循环子串长度次
#             index = magazine.find(ransomNote[i])
#             if index != -1:                                     # 在父串中找到第i个子串的位置
#                 a = magazine[:index] + magazine[index + 1 :]    # 删除父串中第1个子串相同的字母
#
#
#         return a
class Solution:
    def canConstruct(self, a: str, b: str) -> bool:
        set_a = set(a)
        list_a = list(set_a)
        for i in list_a:
            if i not in b or a.count(i) > b.count(i):
                return False
        return True


if __name__ == '__main__':
    ransomNote = "aaaab"
    magazine = "aaaaab"
    print(Solution().canConstruct(ransomNote,magazine))