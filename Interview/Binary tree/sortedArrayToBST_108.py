# @Time :2024/9/5 8:48

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def hepper(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            root.left = hepper(left, mid - 1)
            root.right = hepper(mid + 1, right)
            return root

        return hepper(0, len(nums) - 1)
