# @Time :2024/9/13 15:07

class Solution:
    def firstUniqChar(self, s: str) -> int:
        # 创建一个长度为128的数组，用于存储每个字符的出现次数
        chars = [0] * 128

        # 遍历字符串，统计每个字符的出现次数
        for char in s:
            chars[ord(char)] += 1

        # 再次遍历字符串，找到第一个出现次数为1的字符
        for i, char in enumerate(s):
            if chars[ord(char)] == 1:
                return i

        # 如果没有找到唯一字符，返回-1
        return -1
