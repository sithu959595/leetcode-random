class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        free=[]
        free.append(startTime[0])
        for i in range(len(startTime)-1):
            free.append(startTime[i+1]-endTime[i])
        free.append(eventTime-endTime[-1])
        print(free)
        extra=startTime[0]+(eventTime-endTime[-1])
        res=0
        l=r=0
        cur=free[r]
        while(r<len(free)):
            while((r-l+1)<(k+1)):
                r+=1
                cur+=free[r]
            
            res=max(res,cur)
            print("hi")
            r+=1
            if(r==len(free)):
                break
            cur+=free[r]
            cur-=free[l]
            l+=1
        print(res)
        return res


sol=Solution()
eventTime = 10
k = 1
startTime = [0,2,9]
endTime = [1,4,10]

eventTime = 5
k = 1
startTime = [1,3]
endTime = [2,5]
sol.maxFreeTime(eventTime,k,startTime,endTime)