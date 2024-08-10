# @Time :2024/8/12 11:05
from typing import List


from typing import List

class Solution:
    def __init__(self):
        self.temp = []
        self.ans = []

    def combine(self, n: int, k: int) -> List[List[int]]:
        self.dfs(1, n, k)
        return self.ans

    def dfs(self, cur: int, n: int, k: int) -> None:
        # 剪枝：temp 长度加上区间 [cur, n] 的长度小于 k，不可能构造出长度为 k 的 temp
        if len(self.temp) + (n - cur + 1) < k:
            return
        # 记录合法的答案
        if len(self.temp) == k:
            self.ans.append(self.temp.copy())
            return
        # 考虑选择当前位置
        self.temp.append(cur)
        self.dfs(cur + 1, n, k)
        self.temp.pop()
        # 考虑不选择当前位置
        self.dfs(cur + 1, n, k)