# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        t1=head
        if t1==None:
            return t1
        t2 = t1.next
        if t2 == None:
            return t1
        t3 = t2.next
        t1.next = None

        while t3!=None:
            t2.next = t1
            t1 = t2
            t2 = t3
            t3 = t3.next
        
        t2.next=t1
        return t2