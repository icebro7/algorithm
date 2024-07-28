import collections
from typing import List


# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         L = len(strs)
#         if L <= 1:
#             return [strs]
#
#         for i in range(L):
#             key = "".join(sorted(i))
#             print(key)




# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         mp = collections.defaultdict(list)
#
#         for st in strs:
#             counts = [0] * 26
#             for ch in st:
#                 counts[ord(ch) - ord("a")] += 1
#             # 需要将 list 转换成 tuple 才能进行哈希
#             mp[tuple(counts)].append(st)
#
#         return list(mp.values())

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        HM=dict()
        for i in strs:
            key="".join(sorted(i))
            if key in HM:
                HM[key].append(i)
            else:
                HM[key]=[i]
        return list(HM.values())








if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    # strs = [""]
    print(Solution().groupAnagrams(strs))

