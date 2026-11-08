class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        res=meetings[0][0]-1
        hold=meetings[0][1]
        for i in range(1,len(meetings)):
            cur=meetings[i]
            if(cur[0]>hold):
                res+=cur[0]-hold-1 
                hold=cur[1]
            else:
                if(cur[1]>hold):
                    hold=cur[1]
        return res+(days-hold)
        

------
  -------