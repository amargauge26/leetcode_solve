# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        midnode = self.mid(head)

        revmid = self.revlist(midnode)


        while revmid!= None:
            if head.val!=revmid.val:
                return False

            head = head.next
            revmid = revmid.next
        
        return True


    

    def mid(self,hnode):
        fast = hnode
        slow = hnode

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow 

    def revlist(self,hnode):
        temp = hnode

        prev = None 

        while temp!= None :
            front = temp.next
            temp.next = prev
            prev = temp 
            temp= front
        return prev
