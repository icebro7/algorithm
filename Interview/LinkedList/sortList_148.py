# @Time :2024/9/4 9:27

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        slow,fast = head,head.next
        while fast and fast.next:
            slow,fast  =slow.next,fast.next.next
        mid,slow.next = slow.next,None

        left = self.sortList(head)
        right = self.sortList(mid)

        dummy = current = ListNode(0)
        while left and right:
            if left.val < right.val:
                current.next,left = left,left.next
            else:
                current.next,right = right,right.next
            current = current.next
        current.next = left or right

        return dummy.next