# @Time :2024/7/25 16:11
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        curr = root
        while curr:
            rightmost = curr.left
            while rightmost.right:
                rightmost = rightmost.right

            rightmost.right = curr.right
            curr.right = curr.left
            curr.left = None

        curr = curr.right


