class Solution:
    def findingUsersActiveMinutes(self, logs: list[list[int]], k: int) -> list[int]:
        l={}
        c={}
        res=[0]*k
        for each in logs:
            l[each[0]]=l.get(each[0],set())
            if(each[1] not in l[each[0]]):
                c[each[0]]=c.get(each[0],0)+1
                l[each[0]].add(each[1])
        print(l)
        print(c)
        for each in c:
            res[c[each]-1]+=1
        return res


sol=Solution()
logs = [[0,5],[1,2],[0,2],[0,5],[1,3]]
k = 5

logs = [[1,1],[2,2],[2,3]]
k = 4
print(sol.findingUsersActiveMinutes(logs,k))