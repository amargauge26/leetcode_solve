class Solution:
    def climbStairs(self, n: int) -> int:
        dp =[-1]*(n+1)
        
        return self.c(n,dp)
    def c(self,ind,dp):
        if ind ==0:
            return 1
        if ind <0:
            return 0

        if dp[ind]!=-1:
            return dp[ind]
        t1 = self.c(ind-1,dp)

        t2 = self.c(ind-2,dp)
        
        dp[ind]=t1 + t2

        return dp[ind]