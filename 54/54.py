class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        moves=[(0,1),(1,0),(0,-1),(-1,0)]
        visited=set()
        res=[]
        def dfs(cur,m):
            (row,col)=cur
            visited.add((row,col))
            # nrow,ncol=(row+moves[m][0]),(col+moves[m][1])
                # nrow,ncol=(row+moves[m][0]),(col+moves[m][1])
            res.append(matrix[row][col])
            nrow,ncol=(row+moves[m][0]),(col+moves[m][1])
            if(nrow<0 or nrow>=len(matrix) or ncol<0 or ncol>=len(matrix[0]) or (nrow,ncol) in visited): #change direction
                m=(m+1)%4
                nrow,ncol=(row+moves[m][0]),(col+moves[m][1])
                if(nrow>=0 and nrow<len(matrix) and ncol>=0 and ncol<len(matrix[0]) and (nrow,ncol) not in visited):
                    dfs((nrow,ncol),m)
            else:
                dfs((nrow,ncol),m)
        dfs((0,0),0)
        return res
