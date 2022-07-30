# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        newhead = ListNode(0)
        lesser = newhead
        greater = ListNode(0)
        grt = greater
        while(head):
            if head.val<x:
                lesser.next = ListNode(head.val)
                lesser = lesser.next
            else:
                grt.next = ListNode(head.val)
                grt = grt.next
            head = head.next
            
        lesser.next = greater.next
        
        return newhead.next