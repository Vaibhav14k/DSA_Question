from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def _init_(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        arr=[]
        while head:
            arr.append(head.val)
            head = head.next
        temp = arr[:left-1] + list(reversed(arr[left-1:right])) + arr[right:]
        head2 = temp2 = ListNode()
        for i in temp:
            temp2.next = ListNode(i)
            temp2 = temp2.next
        return head2.next