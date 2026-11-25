class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited=[[False]*len(grid[0]) for _ in range(len(grid))]
        def dfs(cur):
            [ROW,COL]=cur
            #top,right,bottom,left
            moves=[[-1,0],[0,1],[1,0],[0,-1]]
            for m in moves:
                row,col=ROW+m[0],COL+m[1]
                if(row>=0 and row<len(grid) and col>=0 and col<len(grid[0]) and not visited[row][col] and grid[row][col]=="1"):
                    visited[row][col]=True  
                    dfs([row,col])
        res=0
        for rr in range(len(grid)):
            for cc in range(len(grid[0])):
                if(grid[rr][cc]=="1"):
                    res+=1
                    dfs([rr,cc])