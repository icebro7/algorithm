import time
from typing import List


# class Solution:
#     def hIndex(self, citations: List[int]) -> int:
#         L = len(citations)
#         if L < 1:
#             return 0
#         if L % 2 ==0:
#             juge = L / 2
#         else:
#             juge = int(L / 2) + 1
#         citations.sort()
#         mid = citations[juge - 1]
#         return mid

        # for i in range(L):      #求中位数，并且记录大于中位数的个数
        #     citations[i]

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        cnt = [0] * (n + 1)
        for c in citations:
            cnt[min(c, n)] += 1  # 引用次数 > n，等价于引用次数为 n
        s = 0
        for i in range(n, -1, -1):  # i=0 的时候，s>=i 一定成立
            s += cnt[i]
            if s >= i:  # 说明有至少 i 篇论文的引用次数至少为 i
                return i


if __name__ == '__main__':
    s_time = time.time()
    citations = [1,3,1]
    print(Solution().hIndex(citations))
    e_time = time.time()
    a_time = e_time - s_time
    print(a_time)