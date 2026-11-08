class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        visited=set()
        nei={each:[] for each in range(n)}
        reach={each:[] for each in range(n)}
        unreach=0
        result=0
        for j in edges:
            l=j[0]
            r=j[1]
            nei[l].append(r)
            nei[r].append(l)
        def dfs(cur,re):
            re.add(cur)
            visited.add(cur)
            neighbours=nei[cur]
            for k in neighbours:
                if k not in visited:
                    dfs(k,re)
        for i in range(n):
            if( i not in visited):
                re=set()
                dfs(i,re)
                result+=(len(re)*(n-len(re)))-((unreach)*len(re))
                unreach+=len(re)
                # for m in range(n):
                #     if(m not in re):
                #         unreach[m]+=len(re)
        return result


# class Solution:
#     def countPairs(self, n: int, edges: List[List[int]]) -> int:
#         visited=set()
#         nei={each:[] for each in range(n)}
#         reach={each:[] for each in range(n)}
#         pair=set()
#         for j in edges:
#             l=j[0]
#             r=j[1]
#             nei[l].append(r)
#             nei[r].append(l)
#         def dfs(cur,re):
#             visited.add(cur)
#             neighbours=nei[cur]
#             for k in neighbours:
#                 if k not in visited:
#                     re.append(k)
#                     dfs(k,re)
#         for i in range(n):
#             # visited.add(i)
#             if(i not in visited):
#                 re=[i]
#                 dfs(i,re)
#                 #copy the reach to reach of i
#                 for e in re:
#                     reach[e]=re
#             for m in range(n):
#                 if(m!=i and (m not in reach[i])):
#                     pair.add((min(m,i),max(m,i)))
#         return len(pair)