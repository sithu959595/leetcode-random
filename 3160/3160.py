class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        bToc={}     #ball to colors
        colors={} #color count
        res=[]
        for i in range(len(queries)):
            b=queries[i][0]
            c=queries[i][1]
            colors[c]=colors.get(c,0)+1
            if(b in bToc):     #reduce for old color and put new color
                colors[bToc[b]]-=1
                if(colors[bToc[b]]==0):
                    del colors[bToc[b]]
                bToc[b]=c
            else:
                bToc[b]=c
            res.append(len(colors))
        return res
                
