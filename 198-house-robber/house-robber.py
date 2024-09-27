class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1]*len(nums)
        return self.maxii(len(nums)-1,dp,nums)

    
    def maxii(self,ind,dp,arr):
        if ind ==0:
            return arr[ind]
        if ind<0:
            return 0

        if dp[ind]!=-1:
            return dp[ind]

        pick = arr[ind] + self.maxii(ind-2,dp,arr)


        notpick = self.maxii(ind-1,dp,arr)

        dp[ind]= max(pick , notpick)

        return dp[ind]