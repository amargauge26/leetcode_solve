class Solution:
    def findPath(self, m, n):
        # Initialize the visited matrix
        vis = [[0 for _ in range(n)] for _ in range(n)]
        ans = []
        
        # Start the pathfinding from the top-left corner (0, 0)
        if m[0][0] == 1:
            vis[0][0] = 1
            self.path(0, 0, vis, m, "", ans, n)
        
        return ans
    
    def path(self, i, j, vis, m, st, ans, n):
        # If destination is reached, add the path to the answer
        if i == n-1 and j == n-1:
            ans.append(st)
            return
        
        # Move Down
        if i + 1 < n and vis[i+1][j] == 0 and m[i+1][j] == 1:
            vis[i+1][j] = 1
            self.path(i+1, j, vis, m, st + "D", ans, n)
            vis[i+1][j] = 0
        
        # Move Left
        if j - 1 >= 0 and vis[i][j-1] == 0 and m[i][j-1] == 1:
            vis[i][j-1] = 1
            self.path(i, j-1, vis, m, st + "L", ans, n)
            vis[i][j-1] = 0
        
        # Move Right
        if j + 1 < n and vis[i][j+1] == 0 and m[i][j+1] == 1:
            vis[i][j+1] = 1
            self.path(i, j+1, vis, m, st + "R", ans, n)
            vis[i][j+1] = 0
        
        # Move Up
        if i - 1 >= 0 and vis[i-1][j] == 0 and m[i-1][j] == 1:
            vis[i-1][j] = 1
            self.path(i-1, j, vis, m, st + "U", ans, n)
            vis[i-1][j] = 0
