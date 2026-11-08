class UndergroundSystem:

    def __init__(self):
        self.start={}
        self.end={}
        self.record={}
        self.num={}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.start[id]=(stationName,t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        sr=self.start[id]
        s=sr[0]
        e=stationName
        dur=t-sr[1]
        if (s,e) not in self.record:
            self.record[(s,e)]=0
            self.num[(s,e)]=0
        self.record[(s,e)]+=dur
        self.num[(s,e)]+=1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.record[(startStation,endStation)]/self.num[(startStation,endStation)]


# Your UndergroundSystem object will be instantiated and called as such:,
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)