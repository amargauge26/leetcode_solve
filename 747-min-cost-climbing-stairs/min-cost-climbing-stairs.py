class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [-1]*(n+1)
        return min(self.c(n-1,cost,dp),self.c(n-2,cost,dp))

        
    
    def c(self,ind,cost,dp):
        if ind ==0:
            return cost[0]
        if ind ==1:
            return cost[1]
        if ind<0:
            return 0
        
        if dp[ind]!=-1:
            return dp[ind]

        take = cost[ind] + min(self.c(ind-1,cost,dp),self.c(ind-2,cost,dp))
        

        dp[ind]= take

        return dp[ind]
    