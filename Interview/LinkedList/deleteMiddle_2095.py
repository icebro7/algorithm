# @Time :2024/9/21 9:30
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return None
        slow,fast,pre = head,head,None
        while fast and fast.next:
            fast = fast.next.next
            pre = slow
            slow = slow.next
        pre.next = pre.next.next
        return head