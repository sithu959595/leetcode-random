class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        # reduce={}
        # for i in range(len(time)):
        #     cal=time[i]%60
        #     if(cal not in reduce):
        #         reduce[cal]=1
        #     else:
        #         reduce[cal]+=1
        # res=0
        # print(reduce)
        # for j in range(len(time)):
        #     need=60-time[j]
        #     if(need in reduce):
        #         print(j,reduce[need]-1 if need==time[j] else reduce[need])
        #         res+=reduce[need]-1 if need==time[j] else reduce[need]
        # return res
        reduce={}
        res=0
        for i in range(len(time)-1,-1,-1):
            r=(time[i]%60)
            need=0
            if(r):
                need=60-r
            res+=reduce[need] if need in reduce else 0
            if(r in reduce):
                reduce[r]+=1
            else:
                reduce[r]=1
        return res

sol=Solution()
time = [30,20,150,100,40]
# time = [60,60,60]
print(sol.numPairsDivisibleBy60(time))