# @Time :2024/7/28 8:47
from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        rightmost_value = []
        queue = deque([(root, 0)])
        while queue:
            node, depth = queue.popleft()

            if depth == len(rightmost_value):
                rightmost_value.append(node.val)
            else:
                rightmost_value[depth] = node.val

            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))

        return rightmost_value


