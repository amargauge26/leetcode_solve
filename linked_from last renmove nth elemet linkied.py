# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast1 = head
        slow2 = head

        for _ in range(n):
            fast1 = fast1.next

        if fast1 is None:
            return head.next
        
        while fast1.next is not None:
            fast1 = fast1.next
            slow2 = slow2.next
            
        

        delnode = slow2.next

        slow2.next = slow2.next.next
        delnode = None
            
        
        return head
            

