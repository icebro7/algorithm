# @Time :2024/7/27 9:35
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        queue = deque([(root, root.val)])
        while queue:
            node, current_sum = queue.popleft()
            if not node.left and not node.right and current_sum == sum:
                return True

            if node.left:
                queue.append((node.left, current_sum + node.left.val))

            if node.right:
                queue.append((node.right, current_sum + node.right.val))

        return False
