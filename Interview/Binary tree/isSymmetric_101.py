# @Time :2024/7/19 9:11
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def cur(L,R):
            if not L and not R:
                return True
            if not L or not R:
                return False
            if L.val != R.val:
                return False
            return cur(L.left,R.right) and cur(L.right,R.left)
        return cur(root.left,root.right) if root else True
