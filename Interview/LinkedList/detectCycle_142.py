# @Time :2024/9/4 9:01

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast,slow = head,head
        while True:
            if not (fast and fast.next):
                return
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        fast = head
        while fast!= slow:
            fast = fast.next
            slow = slow.next
        return fast