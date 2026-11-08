class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        land=None
        for i in range(len(boxGrid)):
            land=len(boxGrid[0])-1
            for j in range(len(boxGrid[0])-1,-1,-1):
                if(boxGrid[i][j]=="*"):
                    land=j-1
                elif(boxGrid[i][j]=="#"):
                    boxGrid[i][j]="."
                    boxGrid[i][land]="#"
                    land-=1
        print(boxGrid)
        sol=[]
        for k in range(len(boxGrid[0])):
            tem=[]
            for l in range(len(boxGrid)-1,-1,-1):
                tem.append(boxGrid[l][k])
            sol.append(tem)
        return sol


s=Solution()
boxGrid = [["#",".","*","."],["#","#","*","."]]
boxGrid = [["#","#","*",".","*","."],
              ["#","#","#","*",".","."],
              ["#","#","#",".","#","."]]

print(s.rotateTheBox(boxGrid))