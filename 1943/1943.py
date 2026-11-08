import heapq
class Solution:
    def splitPainting(self, segments: list[list[int]]) -> list[list[int]]:
        h=[]
        segments.sort()
        res=[]
        cur=[]
        mix=0
        for i in range(len(segments)):
            mix+=segments[i][2]
            heapq.heappush(h,[segments[i][1],segments[i][2]])
            nextStart=segments[i+1][0] if i+1<len(segments) else float("inf")
            start=segments[i][0]
            end=None
            while(h and h[0][0]<=nextStart):
                end=h[0][0]
                if(end!=start):
                    res.append([start,end,mix])
                    start=end
                mix-=h[0][1]
                heapq.heappop(h)
            if(start<nextStart and mix):
                if(start!=nextStart and i!=len(segments)-1):
                    res.append([start,nextStart,mix])
        return res

sol=Solution()
segments = [[1,4,5],[4,7,7],[1,7,9]]
# segments = [[1,7,9],[6,8,15],[8,10,7]]
segments=[[1,5,1], [2,3,2], [4,6,4]]
print(sol.splitPainting(segments))

