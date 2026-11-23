class Solution:
    def sequentialDigits(self, low: int, high: int) -> list[int]:
        res=[]
        def recur(l,curN,cur):
            curI=int(cur) if cur else 0
            if(curN==10 or len(cur)==l):
                if(curI<=high and curI>=low and len(cur)==l):
                    res.append(curI)
                return
            nn=(curI*10)+curN
            recur(l,curN+1,str(nn))
        LLEN=len(str(low))
        HLEN=len(str(high))
        # start=""
        # startN=None
        # for i in range(1,LLEN+1):
        #     start+=str(i)
        #     startN=i
        for i in range(LLEN,HLEN+1):
            for j in range(1,10):
                recur(i,j,"")
        return res
