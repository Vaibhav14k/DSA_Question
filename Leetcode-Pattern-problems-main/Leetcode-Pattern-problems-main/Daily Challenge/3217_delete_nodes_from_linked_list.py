# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
'''class Solution:
    def modifiedList(self, nums: list[int], head: Optional[ListNode]) -> Optional[ListNode]:
        head2 = temp = ListNode()
        nums = set(nums)
        arr = []
        while head:
            if head.val in nums:
                head = head.next
                continue
            arr.append(head.val)
            head = head.next
        for i in arr:
            temp.next= ListNode(i)
            temp = temp.next
        return head2.next'''
class Solution:
    def modifiedList(self, nums: list[int], head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        nums = set(nums)
        dummy.next = head
        prev,curr = dummy,head
        while curr:
            if curr.val in nums:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return dummy.next