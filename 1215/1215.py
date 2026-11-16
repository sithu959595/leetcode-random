class Solution:
    def countSteppingNumbers(self, low: int, high: int) -> list[int]:

        res=[]
        if(low==0):
            res.append(0)
        # def recur(cur):
        #     if(cur):
        #         last=int(str(cur)[-1])
        #     for n in range(10):
        #         if(not(cur) or n==last-1 or n==last+1):
        #             nn=(cur*10)+n
        #             if(nn<low):
        #                 continue
        #             if(nn>high):
        #                 return res
        #             res.append(nn)
        def recur(cur,l):
            if(l==len(str(cur))):
                if(cur<low):
                    return False
                if(cur>high):
                    return True
                res.append(cur)
                return False
            last=int(str(cur)[-1])
            for j in range(0,10):
                if(j==last-1 or j==last+1):
                    nn=(cur*10)+j
                    if(recur(nn,l)):
                        return True
                    # else:
                    #     return False

                    
            # l-=1
        length=1
        while(True):
            for n in range(1,10):
                if(recur(n,length)):
                    return res
                # cur=n
                # l=length
                # while(not l):
                #     last=int(str(cur)[-1])
                #     for j in range(0,10):
                #         if(j==last-1 or j==last+1):
                #             nn=(cur*10)+j
                #             if(nn<low):
                #                 continue
                #             if(nn>high):
                #                 return res
                #             res.append(nn)
                #     l-=1
            length+=1
