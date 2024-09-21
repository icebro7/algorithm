# @Time :2024/9/4 8:10
from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        A,B = headA,headB
        while A!= B:
            A = A.next if A else headB
            B = B.next if B else headA
        return A




