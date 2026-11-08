class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        res=""
        for cur in s:
            if(not k):
                res+=cur
                continue
            loop=(ord('z')-ord(cur))<(ord(cur)-ord('a'))
            if(loop and (ord('z')+1)-ord(cur)<=k): #can afford a in a loop
                    res+="a"
                    k-=(ord('z')+1)-ord(cur)
                    continue
            #go backward
            if(ord(cur)-ord('a')<=k): #can afford a
                goDis=ord(cur)-ord('a')
            else:
                goDis=k
            k-=goDis
            res+=chr(ord(cur)-goDis)
        return res

sol=Solution()
s = "zbbz"
k = 3
print(sol.getSmallestString(s,k))