class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        i = j = 0
        while i < n and j < m:  #  两个指针交替循环匹配
            if s[i] == t[j]:    #   若该索引上的值相等，则移动子序列的索引
                i += 1
            j += 1  #   否则移动母序列的索引
        return i == n   #   如果查找到的数量与子序列的长度一致，则true
g

if __name__ == '__main__':
    s = "acb"
    t = "ahbgdc"
    print(Solution().isSubsequence(s,t))

