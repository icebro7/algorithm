# @Time :2024/9/21 9:53
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head.next
        while fast.next:
            slow = slow.next
            fast = fast.next.next

        # 反转链表
        last = slow.next
        while last.next:
            cur = last.next
            last.next = cur.next
            cur.next = slow.next
            slow.next = cur

        ans = 0
        x, y = head, slow.next
        while y:
            ans = max(ans, x.val + y.val)
            x, y = x.next, y.next
        return ans
