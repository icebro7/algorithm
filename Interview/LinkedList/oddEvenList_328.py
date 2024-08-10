# @Time :2024/9/21 9:47
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        evenHead = head.next
        odd, even = head, evenHead
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenHead
        return head

if __name__ == '__main__':
    head = [1, 2, 3, 4, 5]
    print(Solution().oddEvenList(head))
