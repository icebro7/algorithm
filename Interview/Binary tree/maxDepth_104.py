# @Time :2024/7/14 16:01
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        else:
            left = self.maxDepth(root.left)
            right = self.maxDepth(root.right)

            return max(left,right) + 1


if __name__ == '__main__':
    root = [3, 9, 20, 0, 0, 15, 7]
    print(Solution().maxDepth(root))
