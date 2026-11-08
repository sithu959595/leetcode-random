import heapq
class Solution:
    def smallestChair(self, times: list[list[int]], targetFriend: int) -> int:
        chairs=[i for i in range(len(times))]
        t=[times[i][:]+[i] for i in range(len(times))] #[arriving time,leaving time, person number]
        t.sort()
        occupy=[]   #[leaving time,chair number]
        # heapq.heapify(chairs)
        print(chairs)
        for each in t:
            while(occupy and occupy[0][0]<=each[0]):
                tem=heapq.heappop(occupy)
                heapq.heappush(chairs,tem[1])
            avail=heapq.heappop(chairs)
            if(each[2]==targetFriend):
                return avail
            heapq.heappush(occupy,[each[1],avail])


sol=Solution()
times = [[1,4],[2,3],[4,6]]
targetFriend = 1

times = [[3,10],[1,5],[2,6]]
targetFriend = 0
print(sol.smallestChair(times,targetFriend))
