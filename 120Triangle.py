class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        dp= [[-1 for _ in range(len(triangle[row]))] for row in range(len(triangle))]
        return self.waysmin(0,0,dp,triangle)

    def waysmin(self,i,j,dp,arr):
        if i==len(arr)-1:
            return arr[i][j]
        
        if dp[i][j]!=-1:
            return dp[i][j]
        
        down = self.waysmin(i+1,j,dp,arr)
        diag = self.waysmin(i+1,j+1,dp,arr)

        dp[i][j]=arr[i][j]+ min(down,diag)

        return dp[i][j]
# top down approch



class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        dp= [[0 for _ in range(len(triangle[row]))] for row in range(len(triangle))]
        dp[len(triangle)-1]=triangle[-1]

        for i in range(len(triangle)-2,-1,-1):
            for j in range(i,-1,-1):
                down = dp[i+1][j]

                diag = dp[i+1][j+1]
                dp[i][j]=min(down,diag)+triangle[i][j]

        return dp[0][0]


bottom up approceh
