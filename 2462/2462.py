import heapq
class Solution:
    def totalCost(self, costs: list[int], k: int, candidates: int) -> int:
        l,r=0,len(costs)-1
        hr=[]
        hl=[]
        # pre=[[costs[i],i] for i in range(len(costs))]
        res=0
        i=0
        while(l<len(costs) and l<r and i<candidates):
            # print("**",costs[l])
            heapq.heappush(hl,costs[l])
            i+=1
            l=i
        l-=1
        i=0
        while(r>=0 and l<r and i<candidates):
            heapq.heappush(hr,costs[r])
            i+=1
            r=len(costs)-1-i
        r+=1
        print(hl,hr,l,r)
        for j in range(k):
            curR=hr[0] if len(hr) else float("inf")
            curL=hl[0] if len(hl) else float("inf")
            print("*",hl,hr,curL,curR)
            if(curL<=curR): #pick left
                res+=curL
                heapq.heappop(hl)
                print("left",curL,l+1,len(costs),r)
                if(l+1<len(costs) and l+1<r):
                    print("l")
                    l+=1
                    heapq.heappush(hl,costs[l])
            else: #puick right
                res+=curR
                heapq.heappop(hr)
                print("right",curR)
                if(r-1>=0 and l<r-1):
                    print("r")
                    r-=1
                    heapq.heappush(hr,costs[r])
        return res

sol=Solution()
costs = [17,12,10,2,7,2,11,20,8]
k = 3
candidates = 4

costs = [1,2,4,1]
k = 3
candidates = 3
print(sol.totalCost(costs,k,candidates))