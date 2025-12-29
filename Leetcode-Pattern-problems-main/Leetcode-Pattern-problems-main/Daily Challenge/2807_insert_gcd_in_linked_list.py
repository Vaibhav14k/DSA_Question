# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        temp = head
        while head and head.next:
            sol = 1
            for i in range(1,min(head.val,head.next.val)+1):
                if head.val % i ==0 and head.next.val % i == 0:
                    sol = i
            head.next = ListNode(sol,head.next)
            head = head.next.next
        return temp
