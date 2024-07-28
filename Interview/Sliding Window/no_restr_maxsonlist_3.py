# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         L = len(s)
#         start,end = 0,0     #上下两个滑动窗口
#         res = ''    #暂存字符
#         n = 1      #存储最短的重复字符串，默认为1，因为已经排除字符为空的情况
#
#
#         if not s:   #做一次判断是否为空
#             return 0
#
#         while end < L:  #若下方滑块还在整个列表当中
#             res += s[end]   #将下方滑块的字符放入
#             len_res = len(res)
#             len_res_set = len(set(res))
#             while len_res != len_res_set:       # 如果暂存的字符有重复的话
#                 n = max(n,len_res - 1)      #将本次循环中字符长度最长的情况记录到n
#                 res = res[start:end]
#                 len_res -= 1
#                 start  += 1
#             end += 1
#
#         return n
#
#     #这个方法只适用字符串中存在这么一子序列，而不是字符串

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 哈希集合，记录每个字符是否出现过
        occ = set()     #设置一个集合（不重复元素数据）
        n = len(s)
        # 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
        rk, ans = -1, 0
        for i in range(n):
            if i != 0:  #循环到此说明已经做完一次完整循环
                # 移除存放在set中的，s最前方字符
                occ.remove(s[i - 1])
            while rk + 1 < n and s[rk + 1] not in occ:
                # 不断地移动右指针
                occ.add(s[rk + 1])
                rk += 1
            # 第 i 到 rk 个字符是一个极长的无重复字符子串
            ans = max(ans, rk - i + 1)
        return ans


if __name__ == '__main__':
    s = ""
    print(Solution().lengthOfLongestSubstring(s))


