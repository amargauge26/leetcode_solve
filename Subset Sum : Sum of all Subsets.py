#User function Template for python3
class Solution:
	def subsetSums(self, arr, n):
		# code here
		res = []
		curr =0
		self.summs(n-1,arr,curr,res)
		return res
	    
	def summs(self,ind,arr,curr,res):
	    if ind <0:
	        res.append(curr)
	        return
	        
	    
	    self.summs(ind-1,arr,curr,res)
	    
	    self.summs(ind-1,arr,curr+arr[ind],res) 
	    
