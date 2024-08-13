# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        fast= head 

        slow = self.dcycle(head)

        if slow is None:
            return None

        
        while slow!=fast:
            if slow == fast:
                return fast
            
            else:
                
                fast = fast.next
                slow = slow.next
            
        return fast


    def dcycle(self,hnode):

        fast = hnode
        slow = hnode

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return slow
        
        return None
