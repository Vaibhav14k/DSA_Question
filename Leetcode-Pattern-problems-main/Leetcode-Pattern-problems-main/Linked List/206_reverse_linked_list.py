# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        prev = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur 
            cur = temp
        return prev



obj = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

print(obj.reverseList(head)) # Output: [1,2,4,5]
while head:
    print(head.val, end=" ")
    head = head.next
