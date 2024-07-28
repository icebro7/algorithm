# @Time :2024/7/24 10:03
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None

        root = TreeNode(postorder[-1])
        stack = [root]
        inorderIndex = len(inorder) - 1

        for value in reversed(postorder[:-1]):
            newNode = TreeNode(value)
            currentNode = stack[-1]

            if currentNode.val != inorder[inorderIndex]:
                currentNode.right = newNode
            else:
                while stack and stack[-1].val == inorder[inorderIndex]:
                    currentNode = stack.pop()
                    inorderIndex -= 1
                currentNode.left = newNode

            stack.append(newNode)

        return root
