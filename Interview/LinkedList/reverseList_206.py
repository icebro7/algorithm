# @Time :2024/9/4 8:33
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = ListNode(0)

        while head:
            next_node = head.next
            head.next = pre.next
            pre.next = head
            head = next_node
        return pre.next