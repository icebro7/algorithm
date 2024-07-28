# @Time :2024/7/18 8:43
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        n = 1
        current = head
        while current.next:
            current = current.next
            n += 1

        k = k % n
        if k == 0:
            return head

        current.next = head
        steps = n - k
        while steps:
            current = current.next
            steps -= 1

        new_head = current.next
        current.next = None

        return new_head
