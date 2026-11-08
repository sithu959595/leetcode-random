class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        if(obstacleGrid[0][0]==1):
            return 0
        # visited=[[None]*len(obstacleGrid[0])]*len(obstacleGrid)
        visited=[[None]*len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]
        d=[1,0]
        r=[0,1]
        # print(visited)
        def dfs(cur):
            ROW,COL=cur[0],cur[1]
            if(ROW==len(obstacleGrid)-1 and COL==len(obstacleGrid[0])-1):
                # print("********")
                paths=0 if obstacleGrid[ROW][COL]==1 else 1
                visited[ROW][COL]=paths
                return paths
            down=[ROW+d[0],COL+d[1]]
            right=[ROW+r[0],COL+r[1]]
            paths=0
            print(cur)
            if(down[0]<len(obstacleGrid) and down[1]<len(obstacleGrid[0]) and obstacleGrid[down[0]][down[1]]!=1):
                print("d",paths,visited)
                paths+=dfs(down) if visited[down[0]][down[1]]==None else visited[down[0]][down[1]]
            if(right[0]<len(obstacleGrid) and right[1]<len(obstacleGrid[0]) and obstacleGrid[right[0]][right[1]]!=1):
                # print("*",right,visited)
                print("r",paths,visited)
                paths+=dfs(right) if visited[right[0]][right[1]]==None else visited[right[0]][right[1]]
            print("assig",cur,visited,ROW,COL,paths)
            visited[ROW][COL]=paths
            print("--------",visited)
            return paths
        dfs([0,0])
        print(visited)
        return visited[0][0]

sol=Solution()

obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
obstacleGrid = [[0,1],[0,0]]
obstacleGrid=[[1]]
obstacleGrid=[[0,0,0,0],[0,1,0,0],[0,0,0,0],[0,0,1,0],[0,0,0,0]]
obstacleGrid=[[0, 0, 0],[0, 0, 0]]
print(sol.uniquePathsWithObstacles(obstacleGrid))