# @Time :2024/7/27 10:17
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, prevTotal: int) -> int:
            if not root:
                return 0
            total = prevTotal * 10 + node.val

            if not node.left and not node.right:
                return total
            else:
                return dfs(node.left,total) + dfs(node.right,total)

        return dfs(root,0)

