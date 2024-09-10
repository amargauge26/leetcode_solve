from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        vis = grid
        m,n = len(grid),len(grid[0])

        q = deque()
        freshcount=0
        for i in range(m):
            for j in range(n):
                if vis[i][j]==2:
                    q.append((i,j))
                
                if vis[i][j]==1:
                    freshcount+=1
        

        if freshcount ==0:
            return 0
        
        if not q :
            return -1
        

        mins=-1
        dirs = [(-1,0),(1,0),(0,1),(0,-1)]
        while q :
            s = len(q)

            while s>0:
                x,y=q.popleft()
                s-=1
                for dx,dy in dirs:
                    i,j = dx+x,dy+y
                    if 0<=i<m and 0<=j<n and vis[i][j]==1:
                        freshcount-=1
                        vis[i][j]=2
                        q.append((i,j))
            mins+=1
        

        if freshcount==0:
            return mins
        
        return -1
        