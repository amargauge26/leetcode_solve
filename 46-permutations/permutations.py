class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans =[]
        ds =[]
        fre=[0]*len(nums)
        self.pp(nums,ans,ds,fre)
        return ans
    
    def pp(self,nums,ans,ds,fre):
        if len(nums)==len(ds):
            ans.append(ds[:])
            return
        
        for i in range(len(nums)):
            if fre[i]==0:
                ds.append(nums[i])
                fre[i]=1
                self.pp(nums,ans,ds,fre)
                ds.pop()
                fre[i]=0



    

