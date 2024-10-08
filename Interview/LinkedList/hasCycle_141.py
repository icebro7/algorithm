# @Time :2024/7/13 8:58
from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if fast is slow:
                return True

        return False

if __name__ == '__main__':
    head = [3, 2, 0, -4]
    pos = 1
    print(Solution().hasCycle(head))