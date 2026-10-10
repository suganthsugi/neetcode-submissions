# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        rem = 0
        result = ListNode()
        tail = result
        while l1 is not None or l2 is not None:
            if l1 is not None and l2 is not None:
                total = l1.val + l2.val + rem
                l1 = l1.next
                l2 = l2.next
            elif l1 is not None:
                total = l1.val + rem
                l1 = l1.next
            elif l2 is not None:
                total = l2.val + rem
                l2 = l2.next
            
            rem = int(total/10)
            total = total%10
            tail.next = ListNode(total)
            tail = tail.next
        if rem!=0:
            tail.next = ListNode(rem)
        return result.next