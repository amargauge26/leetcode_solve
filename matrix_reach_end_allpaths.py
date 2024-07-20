class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        """if not m and not n:
            return 0
        dp = [[1]*n]*m
        for row in range(1,m):
            for col in range(1,n):
                dp[row][col]=dp[row-1][col]+dp[row][col-1]
        return dp[-1][-1]"""
        """ sums=0
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        return self.ways(m-1,n-1,dp)"""
        """"if not m and not n :
            return 0

        dp=[[1]*n]*m
        dp[0][0]=1
        for i in range(1,m):
            for j in range(1,n):
                l = dp[i][j-1]
                u = dp[i-1][j]
                dp[i][j]=l+u
        
        return dp[m-1][n-1]"""

        if not m or not n:
            return 0

        # Initialize a 1D dp array with 1s
        dp = [1] * n

        # Iterate over each row starting from the second one
        for i in range(1, m):
            # Iterate over each column starting from the second one
            for j in range(1, n):
                # Update the dp array
                dp[j] += dp[j - 1]

        # The last element in dp array is the result
        return dp[-1]


    def ways(self,i,j,dp):
        if i==0 and j ==0:
            return 1
        if i<0 or j <0 :
            return 0
        if dp[i][j]!=-1:
            return dp[i][j]
        
        up = self.ways(i-1,j,dp)
        left = self.ways(i,j-1,dp)
        dp[i][j]=up + left
        return dp[i][j]


        
