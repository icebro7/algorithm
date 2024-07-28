

# class Solution:
    # def reverseWords(self, s: str) -> str:
    #     L = len(s)
    #     temp = ""
    #
    #     for i in range(L):
    #         count = s[-i - 1]       # 从尾部开始循环str
    #         if count == " " and temp[0] != " ":        # 如果遍历到空格时，temp增加一个空格
    #             temp = " " + temp
    #             continue
    #         temp += count
    #
    #     return temp
    # 实现的是翻转整个str，并且没有清除空格

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.strip().split()[::-1])
    # 分隔倒序解法

class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()                            # 删除首尾空格
        i = j = len(s) - 1                       # 将指针放置在最后一个位置
        res = []                                 # 存储区
        while i >= 0:
            while i >= 0 and s[i] != ' ':
                i -= 1                           # 搜索首个空格
            res.append(s[i + 1: j + 1])          # 添加单词
            while i >= 0 and s[i] == ' ':
                i -= 1                           # 跳过单词间空格
            j = i                                # j 指向下个单词的尾字符
        return ' '.join(res)                     # 拼接并返回

    # 双指针解法




if __name__ == '__main__':


    s = "luffy is still joyboy"
    print(Solution().reverseWords(s))
