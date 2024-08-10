# @Time :2024/8/14 10:10
from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        total_l = [[] for _ in range( n + 1)]
        total_l[0] = [""]
        total_l[1] = ["()"]

        for i in range(2, n+1):
            l = []
            for j in range(i):  # 遍历 p q ，其中p+q=i-1 , j 作为索引
                now_list1 = total_l[j]  # p = j 时的括号组合情况
                now_list2 = total_l[i-1-j]  # q = (i-1) - j 时的括号组合情况
                for k1 in now_list1:
                    for k2 in now_list2:
                        l.append("(" + k1 + ")" + k2)  # 把所有可能的情况添加到 l 中
            total_l[i] = l

        return total_l[n]
