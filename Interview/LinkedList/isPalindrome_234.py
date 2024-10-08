# @Time :2024/9/4 8:45

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vals = []
        current_node = head

        while current_node is not None:
            vals.append(current_node.val)
            current_node = current_node.next

        return vals == vals[::-1]