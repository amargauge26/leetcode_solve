class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return an integer
	def books(self, A, B):
        
        n = len(A)
        if n<B:
            return -1
        
        
        low = max(A)
        high = sum(A)
        
        
        for pages in range(low,high+1):
            if self.st(A,pages)==B:
                return pages
            
            
        return low
    
    def st(self,arr,p):
        
        n = len(arr)
        student=1
        studentp=0
        for i in range(n):
            if studentp+arr[i]<=p:
                studentp+=arr[i]
            
            else:
                student+=1
                studentp=arr[i]
        return student
        
        
        
