#memoisation 

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [-1]*(amount+1)
        res = self.minways(coins,amount,dp)
        return res if res!=float("inf") else -1

    
    def minways(self,c,a,dp):
        if a==0:
            return 0
        if a <0:
            return float("inf")
        if dp[a]!=-1:
            return dp[a]
        mini= float('inf')

        for coins in c:
            take=1 + self.minways(c,a-coins,dp)
            mini=min(mini,take)
        dp[a]=mini
        return dp[a]
        

