class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    
        n = len(matrix)
        m = len(matrix[0])

        for i in range(n):
            if self.tarfind(matrix[i],0,m-1,target):
                return True
                break
        return False

    def tarfind(self,arr,l,h,t):

        
        
        while l<=h:
            mid = (l+h)//2
            if arr[mid]==t:
                return True
            elif arr[mid]<t:
                l=mid+1

            else :
                h = mid-1
        return False
      #close to tle 


#more optimum

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        n= len(matrix)
        m = len(matrix[0])
        
             
        
        return self.tarfind(matrix,0,(n*m)-1,target,m)

    
    def tarfind(self,arr,l,h,t,m):
        while l<=h:
            mid = (l+h)//2

            i = mid//m
            j = mid%m

            if arr[i][j]==t:
                return True
            
            elif arr[i][j]<t:
                l = mid+1
            
            else:
                h = mid -1
        
        return False

