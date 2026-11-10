class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:
        visited=[[False]*len(grid[0])]*len(grid)
        res=0
        def dfs(cur):
            ROW,COL=cur[0],cur[1]
            isEncalved=True
            #check if it is off boundary. if yes, it is not encalved
            if(ROW<0 or ROW>=len(grid) or COL<0 or COL>=len(grid[0])):
                return [False,0]
            #up,down,left,right
            moves=[[ROW-1,COL],[ROW+1,COL],[ROW,COL-1],[ROW,COL+1]]
            #chech if it is visited or water
            if(visited[ROW][COL] or grid[ROW][COL]==0):
                return [True,0]
            visited[ROW][COL]=True
            cc=1
            # count+=1
            for m in moves:
                # NR,NC=m[0],m[1]
                tem=dfs(m)
                isEncalved=isEncalved and tem[0]
                cc+=tem[1]
            return [isEncalved,cc]
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if(grid[row][col]):
                    t=dfs([row,col])
                    if(t[0]):
                        res+=t[1]
        return res