class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res =[]
        temp=[]
        nums.sort()
        self.sublist(len(nums)-1,nums,res,temp)
        res.sort()
        return res
    
    def sublist(self,ind,nums,res,temp):
        if ind < 0:
            if temp[:] not in res:  # Add this check to avoid duplicates
                res.append(temp[:])
            return
        temp.append(nums[ind])
        
        self.sublist(ind-1,nums,res,temp)
        temp.pop()

        self.sublist(ind-1,nums,res,temp)
