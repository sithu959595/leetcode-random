class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        l,r=0,1
        res=0
        while(l<len(colors)):
            print(l,r)
            curlen=(r-l+1) if r>=l else (len(colors)-(l-r-1))
            preR=colors[r-1] if (r-1)>=0 else colors[-1]
            if(preR==colors[r]):
                while(l!=r):
                    l+=1
                    if(l>=len(colors)):
                        return res
                r=(r+1)%len(colors)

                continue
            if(curlen<k):
                r=(r+1)%len(colors)
            elif(curlen==k):
                print("********************")
                res+=1
                l+=1
                r=(r+1)%len(colors)
        return res

sol=Solution()

colors = [0,1,0,1,0]
k = 3
print(sol.numberOfAlternatingGroups(colors,k))