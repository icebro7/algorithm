# @Time :2024/7/28 9:29
from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        queue = deque([root])
        level_index = 0

        while queue:
            level_node = deque()
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.popleft()

                if level_index % 2 == 0:
                    level_node.append(node.val)
                else:
                    level_node.appendleft(node.val)
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            res.append(list(level_node))
            level_index += 1

        return res



