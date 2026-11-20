class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        res=[]
        intervals.sort()
        i=1
        hold=intervals[0]
        while(i<len(intervals)):
            if(hold[1]<intervals[i][0]):
                res.append(hold)
                hold=intervals[i]
            elif(hold[1]>=intervals[i][0] and hold[1]<intervals[i][1]):
                hold=[hold[0],intervals[i][1]]
            # elif(hold[1]>=intervals[i][0] and hold[1]>=intervals[i][1]):
            i+=1
        res.append(hold)
        return res
