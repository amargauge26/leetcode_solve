class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        t = sum(nums)

        if t%2!=0:

            return False
        
        total = t//2
        dp=[[-1 for i in range(total+1)]for _ in range(n)]

        return self.tf(n-1,nums,total,dp)==1
    
    def tf(self,ind,arr,t,dp):

        if t ==0:
            return 1

        if ind ==0:
            if arr[ind]==t:
                return 1
            else:
              
                return 0
        
        if  dp[ind][t]!=-1:
            return dp[ind][t]

        nottake = self.tf(ind-1,arr,t,dp)

        take =0

        if arr[ind]<=t:
            take = self.tf(ind-1,arr,t-arr[ind],dp)
        
        dp[ind][t]= max(take,nottake)

        return dp[ind][t]
        
