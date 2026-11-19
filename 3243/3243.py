from collections import deque
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        route={}
        for i in range(n-1):
            route[i]=[i+1]
        def bfs():
            print(route)
            s=0
            q=deque([0])
            visited=set()
            ac=1
            while(q):
                print(q)
                s+=1
                tem=ac
                ac=0
                for _ in range(tem):
                    cur=q.popleft()
                    for each in route[cur]:
                        if(each==n-1):
                            return s
                        if(each not in visited):
                            visited.add(each)
                            q.append(each)
                            ac+=1
        res=[]
        for query in queries:
            route[query[0]].append(query[1])
            r=bfs()
            res.append(r)
        return res


sol=Solution()
n = 5 
queries = [[2,4],[0,2],[0,4]]
print(sol.shortestDistanceAfterQueries(n,queries))