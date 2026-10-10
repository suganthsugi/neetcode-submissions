# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        t=head
        while t:
            length+=1
            t=t.next
        if length==n:
            return head.next
        
        t=length-n-1
        t1 = head
        while t>0:
            t1=t1.next
            t-=1
        
        if t1.next:
            t1.next = t1.next.next
        else:
            t1.next = None
        return head
