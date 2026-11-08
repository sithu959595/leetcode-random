class Solution:
    def minimumSteps(self, s: str) -> int:
        black=[]
        ans=0
        s1=[]
        cur=0
        for j in range(len(s)):
            if(s[j]=="1"):
                black.append(j)
            elif(s[j]=="0" and len(black)):
                # print("hi",black)
                b=black[cur]
                cur+=1
                # black=black[1:]
                ans+=j-b
                black.append(j)
        return ans

sol=Solution()
s = "101"
s = "100"
# s = "0111"
print("--",sol.minimumSteps(s))