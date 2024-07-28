# @Time :2024/7/24 9:17
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        stack = [root]
        inorderIndex = 0

        for value in preorder[1:]:
            currentNode = stack[-1]
            newNode = TreeNode(value)

            if currentNode.val != inorder[inorderIndex]:
                currentNode.left = newNode

            else:
                while stack and stack[-1].val == inorder[inorderIndex]:
                    currentNode = stack.pop()
                    inorderIndex += 1

                currentNode.right = newNode

            stack.append(newNode)

        return root
