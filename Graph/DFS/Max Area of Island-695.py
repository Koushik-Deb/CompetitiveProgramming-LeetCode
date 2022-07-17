class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        maxTotal = [0]
        
        visited = [[0]*len(grid[0]) for i in range(len(grid))]
        
        dx = [1,0,-1,0]
        dy = [0,1,0,-1]
        
        ROW = len(grid)
        COL = len(grid[0])
        
        def valid(x,y):
            return 0<=x<ROW and 0<=y<COL
        
        def dfs(x,y,count=1):
            # print(x,y,maxTotal)
            maxTotal[0] = max(maxTotal[0], count)
            for i in range(4):
                newX = x+dx[i]
                newY = y+dy[i]
                
                if valid(newX,newY) and grid[newX][newY] and not visited[newX][newY]:
                    visited[newX][newY] = 1
                    count = dfs(newX,newY,count+1)
            
            return count
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j]==1 and visited[i][j]==0:
                    visited[i][j]=1
                    dfs(i,j)
        
        return maxTotal[0]