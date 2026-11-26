from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # visited=[[False]*len(grid[0]) for _ in range(len(grid))]
        time=0
        def bfs(q):
            nonlocal time
            tt=0
            # q=deque(position)
            count=len(q)
            nextC=0
            while(count):
                cur=q.popleft()
                [ROW,COL]=cur
                count-=1
                #up,right,bottom,left
                moves=[[-1,0],[0,1],[1,0],[0,-1]]
                for m in moves:
                    row,col=ROW+m[0],COL+m[1]
                    if(row>=0 and row<len(grid) and col>=0 and col<len(grid[0]) and grid[row][col]==1):
                        nextC+=1
                        grid[row][col]=2
                        q.append([row,col])
                if(not count):
                    time+=1
                    count=nextC
                    nextC=0
        qq=deque()
        for rr in range(len(grid)):
            for cc in range(len(grid[0])):
                if(grid[rr][cc]==2):
                    qq.append([rr,cc])
        bfs(qq)
        for rr in range(len(grid)):
            for cc in range(len(grid[0])):
                if(grid[rr][cc]==1):
                    return -1
        return time