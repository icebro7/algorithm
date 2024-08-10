# @Time :2024/7/31 8:55
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        stack = []
        curr = root
        prev_val = None
        min_diff = float('inf')

        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left

            else:
                curr = stack.pop()
                if prev_val is not None:
                    min_diff = min(min_diff,abs(curr.val - prev_val))
                prev_val = curr.val
                curr = curr.right

        return min_diff



