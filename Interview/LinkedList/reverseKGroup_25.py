# @Time :2024/7/17 8:36
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        node_count = 0
        current = head

        while current:
            node_count += 1
            current = current.next

        dummy_head = ListNode(next = head)
        group_start = dummy_head
        prev = None
        current = head

        while node_count >= k:
            node_count -= k
            for _ in range(k):
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node

            next_group_start = group_start.next
            next_group_start.next = current
            group_start.next = prev
            group_start = next_group_start

        return dummy_head.next
