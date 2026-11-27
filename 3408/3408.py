import heapq
class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.valid={}  #taskId->[priority,userID]
        self.h=[[-p,-t,u] for [u,t,p] in tasks]   #priority,taskid,userid
        # self.t={}
        for each in self.h:
            [p,t,u]=each
            self.valid[t]=[p,u]
        heapq.heapify(self.h)


    def add(self, userId: int, taskId: int, priority: int) -> None:
        # self.valid.add((-taskId,-priority))
        heapq.heappush(self.h,[-priority,-taskId,userId])
        self.valid[-taskId]=[-priority,userId]

    def edit(self, taskId: int, newPriority: int) -> None:
        self.valid[-taskId][0]=-newPriority
        ou=self.valid[-taskId][1]
        heapq.heappush(self.h,[-newPriority,-taskId,ou])

    def rmv(self, taskId: int) -> None:
        # print(taskId,self.valid)
        del self.valid[-taskId]
        # print(taskId,self.valid)

    def execTop(self) -> int:
        cur=heapq.heappop(self.h)
        while(cur[1] not in self.valid or cur[0]!=self.valid[cur[1]][0] or cur[2]!=self.valid[cur[1]][1]): #was it removed or stalled
            if(not self.h):
                return -1
            cur=heapq.heappop(self.h)
        print(cur,self.valid)
        del self.valid[cur[1]]
        return cur[2]
            

# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()