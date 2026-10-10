# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes = []

        t=head
        while t:
            nodes.append(t)
            t1 = t
            t = t.next
            t1.next = None
        
        t1, t2 = 1, len(nodes)-1
        head = nodes[0]
        tail = head
        while t1 < t2:
            tail.next = nodes[t2]
            t2-=1
            tail = tail.next
            tail.next = nodes[t1]
            t1+=1
            tail = tail.next
        if t1==t2:
            tail.next=nodes[t1]
        
    