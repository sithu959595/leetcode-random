import heapq
class FreqStack:

    def __init__(self):
        # self.map={} 
        # self.co=[]
        # self.r=[]
        self.stack=[]
        self.latest={}
        self.heap=[]
        self.count={}
        heapq.heapify(self.heap)

    def push(self, val: int) -> None:
        c=self.count[val] if val in self.count else 0
        c+=1
        ntuple=(-c,-len(self.stack),val)
        self.count[val]=c
        self.latest[val]=len(self.stack)
        heapq.heappush(self.heap,ntuple)
        self.stack.append(val)



    def pop(self) -> int:
        cur=heapq.heappop(self.heap)
        i=cur[1]
        i=-i
        v=cur[2]
        self.count[v]-=1
        self.stack[i]=None
        return cur[2]


# # Your FreqStack object will be instantiated and called as such:
# # obj = FreqStack()
# # obj.push(val)
# # param_2 = obj.pop() 



# import heapq
# import itertools

# counter = itertools.count()
# heap = []

# heapq.heappush(heap, (1, next(counter), "a"))
# heapq.heappush(heap, (1, next(counter), 10))

# print(heapq.heappop(heap))  # (1, 0, 'a')