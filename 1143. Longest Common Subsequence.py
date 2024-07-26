class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[-1 for i in range(len(text2))]for _ in range(len(text1))]

        return self.ll(len(text1)-1,len(text2)-1,text1,text2,dp)
    
    def ll(self,ind1,ind2,text1,text2,dp):

        if ind1<0 or ind2<0:
            return 0

        if dp[ind1][ind2]!=-1:
            return dp[ind1][ind2]    
        
        if text1[ind1]==text2[ind2]:
            dp[ind1][ind2] = 1 + self.ll(ind1-1,ind2-1,text1,text2,dp)
            return dp[ind1][ind2]
        else:dp[ind1][ind2]=0+max(self.ll(ind1-1,ind2,text1,text2,dp),self.ll(ind1,ind2-1,text1,text2,dp))
        return dp[ind1][ind2]
