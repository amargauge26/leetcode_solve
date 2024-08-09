# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        """prev = None
        temp = head

        while temp:
            node3 = temp.next

            temp.next = prev

            prev = temp 
            #when ever it reches the the end prev willl be pointing to the None
            temp =node3
        
        return prev"""

        # more optimisation 
        return  self.rev(head)

    def rev( self,node):
        if not node or not node.next:
            return node
        
        newhead = self.rev(node.next)
        fro = node.next
        fro.next = node
        node.next=None

        return newhead
            
