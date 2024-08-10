# @Time :2024/9/21 10:13
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        f, g = collections.defaultdict(int), collections.defaultdict(int)
        q = collections.deque([(root, None)])
        while len(q) > 0:
            node, parent = q.popleft()
            if parent:
                if parent.left == node:
                    f[node] = g[parent] + 1
                else:
                    g[node] = f[parent] + 1
            if node.left:
                q.append((node.left, node))
            if node.right:
                q.append((node.right, node))

        maxans = 0
        for _, val in f.items():
            maxans = max(maxans, val)
        for _, val in g.items():
            maxans = max(maxans, val)
        return maxans

