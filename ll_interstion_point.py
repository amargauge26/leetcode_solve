# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        #tle
        '''while headB !=None:

            temp = headA
            while temp!=None:
                if temp== headB:
                    return headB
                temp = temp.next
            headB= headB.next

        return None'''
        # hashing solutions 
        """hash = set()

        while headA is not None :
            hash.add(headA)
            headA=headA.next
        
        while headB is not None:
            if headB in hash:
                return headB
            headB = headB.next
        return None"""
        
        diff = self.lenn(headA,headB)

        if diff <0:
            while diff !=0:
                headB = headB.next
                diff+=1
        
        else:
            while diff !=0:
                headA= headA.next
                diff-=1

        while headA != None  :
            if headA== headB:
                return headA
            headB = headB.next
            headA = headA.next

        return headA


    def lenn(self,h1,h2):
        len1 = 0
        len2 = 0
        while h1 is not None:
            len1 += 1
            h1 = h1.next
        
        # Traverse h2 to get its length
        while h2 is not None:
            len2 += 1
            h2 = h2.next
        
        return len1 - len2 

    
