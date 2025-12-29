from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        print(arr)
        arr.sort()
        head2 = temp = ListNode()
        for i in arr:
            temp.next = ListNode(i)
            temp = temp.next
        return head2.next
