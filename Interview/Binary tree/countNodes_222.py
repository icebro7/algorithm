# @Time :2024/7/27 11:22
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def height(self, root: TreeNode) -> int:
        height = 0
        while root:
            root = root.left
            height += 1
        return height

    def countNodes(self, root: TreeNode) -> int:

        if not root:
            return 0

        leftHeight = self.height(root.left)
        rightHeight = self.height(root.right)

        if leftHeight == rightHeight:

            return (1 << leftHeight) - 1 + self.countNodes(root.right) + 1

        else:

            return (1 << rightHeight) - 1 + self.countNodes(root.left) + 1
