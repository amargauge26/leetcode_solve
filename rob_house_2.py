class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        
        if not nums:
            return 0
        
        af = []
        al = []
        dp1=[-1]*(len(nums))
        dp2=[-1]*(len(nums))
        for i in range(len(nums)):
            if i!=0:
                al.append(nums[i])
            if i!=len(nums)-1:
                af.append(nums[i])
            
        f = self.money(len(nums)-2,af,dp1)
        l = self.money(len(nums)-2,al,dp2)

        return max(f,l)
    
    def money(self,ind,arr,dp):
        if ind==0:
            arr[ind]
        if ind<0:
            return 0
        if dp[ind]!=-1:
            return dp[ind]
        
        t = arr[ind]+self.money(ind-2,dp,arr)
        nt = 0 + self.money(ind-1,dp,arr)

        dp[ind]=max(t,nt)

        return dp[ind]


