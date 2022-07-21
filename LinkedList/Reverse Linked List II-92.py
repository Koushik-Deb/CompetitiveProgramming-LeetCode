# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
#Less complicated
        cur = head
        pointer = 1
        prev = None
        
        while pointer!=left:
            prev = cur
            cur = cur.next
            pointer+=1
            
        startPointer = cur
        reversedPointer = None
        
        while pointer!=right+1:
            pointer+=1
            next = cur.next
            cur.next = reversedPointer
            reversedPointer = cur
            cur = next
        
        if prev:
            prev.next = reversedPointer
        startPointer.next = cur
        
        return head if prev else reversedPointer #this condition is true if reverse start from first node.



#Recursive
#         if not head: return None
        
#         lt, rt = head,head
#         stop = False
        
#         def recurseAndReverse(rt, m, n):
#             nonlocal lt, stop
            
#             if n==1:
#                 return
            
#             rt = rt.next
#             if m>1: lt = lt.next
                
#             recurseAndReverse(rt, m-1, n-1)
            
#             if lt==rt or rt.next == lt:
#                 stop = True
            
#             if not stop:
#                 lt.val, rt.val = rt.val, lt.val
#                 lt = lt.next
        
#         recurseAndReverse(rt, left, right)
#         return head


# iterative
        # cur = head
        # pointer = 1
        # prev = None
        
        # while pointer!=left:
        #     prev = cur
        #     cur = cur.next
        #     pointer+=1
            
        # startPointer = cur
        # reversedPointer = prev
        
        # while pointer!=right+1:
        #     pointer+=1
        #     next = cur.next
        #     cur.next = prev
        #     prev = cur
        #     cur = next
        
        # if reversedPointer:
        #     reversedPointer.next = prev
        # else:
        #     head = prev

        # startPointer.next = cur
        
        # return head