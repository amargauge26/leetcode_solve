class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dum = ListNode()
        temp =  dum

        c  =0 
        while (l1 !=None or l2 !=None) or c:
            sum =0
            if l1 is not None :
                sum +=l1.val
                l1 = l1.next
            
            if l2 is not None :
                sum+=l2.val
                l2 = l2.next
            

            sum +=c

            c = sum//10#carry 
            newNode  = ListNode(sum%10)
            temp.next = newNode
            temp = temp.next
        
        return dum.next

