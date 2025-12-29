from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def _init_(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        
        n = len(arr)
        diff = n%k

        sol=[]

        for i in range (0,n-diff,k):
            sol+=list(reversed(arr[i:i+k]))

        sol+=arr[n-diff:]
        
        head2 = temp = ListNode()

        for i in sol:
            temp.next = ListNode(i)
            temp = temp.next
        
        return head2.next