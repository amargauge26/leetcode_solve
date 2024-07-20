class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        i=len(obstacleGrid)
        j=len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[i-1][j-1] == 1:
            return 0
        dp = [[1 for _ in range(j)] for _ in range(i)]

         # Initialize the first column
        for p in range(1, i):
            dp[p][0] = 0 if obstacleGrid[p][0] == 1 else dp[p-1][0]
        
        # Initialize the first row
        for k in range(1, j):
            dp[0][k] = 0 if obstacleGrid[0][k] == 1 else dp[0][k-1]
        
        for p in range(1,i):
            for k in range(1,j):
                if obstacleGrid[p][k]==1:
                    dp[p][k]=0
                else:
                    dp[p][k]=dp[p][k-1]+dp[p-1][k]

        return dp[i-1][j-1]
        
    
    def ways(self,arr,i,j,dp):
        if i < 0 or j < 0:
            return 0
        if arr[i][j] == 1:
            return 0
        if i == 0 and j == 0:
            return 1
        if dp[i][j] != -1:
            return dp[i][j]
        
        up = self.ways(arr,i-1,j,dp)
        left = self.ways(arr,i,j-1,dp)

        dp[i][j]= up+left

        return dp[i][j]
