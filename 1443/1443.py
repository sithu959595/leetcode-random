class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        nei={i:[] for i in range(n)}
        visited=set()
        for edge in edges:
            # if(edge[0] not in nei):
            #     nei[edge[0]]=[]
            nei.get(edge[0]).append(edge[1])
            nei.get(edge[1]).append(edge[0])
        def dfs(cur):
            visited.add(cur)
            tem=0
            print(cur)
            for each in nei[cur]:
                if(each not in visited):
                    tem+=dfs(each)
            if(cur!=0):
                if(tem or hasApple[cur]):
                    tem+=2
            return tem
        return dfs(0)





sol=Solution()
n = 7
edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]

hasApple = [False,False,True,False,True,True,False]

n = 7
edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
hasApple = [False,False,True,False,False,True,False]
print(sol.minTime(n,edges,hasApple))
