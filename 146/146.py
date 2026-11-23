class LRUCache:

    def __init__(self, capacity: int):
        self.d={}
        self.size=capacity
        self.lru=None
        self.mru=None
    def removeLRU(self):
        oldlru=self.lru
        #create a new lru
        self.lru=self.d[oldlru][2]
        #change the new lru's pre
        self.d[self.lru][1]=None
    def makeMRU(self,key,value):
        #change the pre and next of the neighbours
        if(key in self.d):
            pre=self.d[key][1]
            nex=self.d[key][2]
            if(pre):
                self.d[pre][2]=nex
            if(nex):
                self.d[nex][1]=pre
        #change the old mru's next
        oldmru=self.mru
        if(oldmru):
            self.d[oldmru][2]=key
        #change the new mru value's pre and next
        tem=[value,oldmru,None]
        self.d[key]=tem
        #create a new mru
        self.mru=key
        if(len(self.d)==1):
            self.lru=key

    def get(self, key: int) -> int:
        print("get",key)
        if(key not in self.d):
            return -1
        else:
            if(self.lru==key):
                self.removeLRU()
            self.makeMRU(key,self.d[key][0])
            return self.d[key][0]

    def put(self, key: int, value: int) -> None:
        print("put",key,value)
        if(len(self.d)<self.size):
            self.makeMRU(key,value)
        else:
            self.removeLRU()
            del self.d[key]
            self.makeMRU(key,value)
    
##get
#make the key mru
#if key is lru, updte lru

##put
#if full,remove lru and update lru
#make the key mru
#

#removeLru, makeMru
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)