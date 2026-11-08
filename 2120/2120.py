class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        move=((0,-1),(0,1),(-1,0),(1,0))   #L,R,U,D
        L,R,U,D=(0,-1),(0,1),(-1,0),(1,0)
        res=[0 for _ in range(len(s))]
        for i in range(len(s)):
            cur=startPos[:]
            for j in range(i,len(s)):
                if(s[j]=="L"):
                    cur[0]=cur[0]+L[0]
                    cur[1]=cur[1]+L[1]
                elif(s[j]=="R"):
                    cur[0]=cur[0]+R[0]
                    cur[1]=cur[1]+R[1]
                elif(s[j]=="U"):
                    cur[0]=cur[0]+U[0]
                    cur[1]=cur[1]+U[1]
                elif(s[j]=="D"):
                    cur[0]=cur[0]+D[0]
                    cur[1]=cur[1]+D[1]
                if(cur[0]>=n or cur[1]>=n or cur[0]<0 or cur[1]<0):
                    break
                else:
                    res[i]+=1
        return res

sol=Solution()
n = 3
startPos = [0,1]
s = "RRDDLU"
print(sol.executeInstructions(n,startPos,s))
                