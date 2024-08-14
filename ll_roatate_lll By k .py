# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        #upper code tle
        if head ==None or head.next ==None:
            return  head
        
        count =  0
        t = head
        while t!=None:
            t = t.next
            count+=1
        
        if count<k:
            rot = k%count
        else :rot =k
        
        for i in range(rot):
            temp = head

            while temp.next.next!=None:
                temp = temp.next
            
            end = temp.next
            temp.next = None
            end.next = head

            head =end
        
        return head
