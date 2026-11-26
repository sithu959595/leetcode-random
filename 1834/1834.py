import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        mtasks=[]
        for i in range(len(tasks)):
            heapq.heappush(mtasks,[tasks[i][0],tasks[i][1],i])
        fin=mtasks[0][0]
        res=[]
        availbe=[]
        cur=0
        while(mtasks or availbe):
            #find availbe task in mtasks
            while(mtasks and mtasks[0][0]<=fin):
                c=heapq.heappop(mtasks)
                heapq.heappush(availbe,c[1:3])
            #pop from q
            if(availbe):
                cur=heapq.heappop(availbe)
                res.append(cur[1])
                fin+=cur[0]
            else:
                if(mtasks):
                    fin=mtasks[0][0]
        return res