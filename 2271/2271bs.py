class Solution:
    def maximumWhiteTiles(self, tiles: list[list[int]], carpetLen: int) -> int:
        tiles.sort()
        def helper(target):
            print("looking for",target)
            l,r=0,len(tiles)-1
            while(l<=r):
                m=(l+r)//2
                if(tiles[m][0]==target):
                    return m
                elif(target<tiles[m][0]):
                    r=m-1
                else:
                    l=m+1
            return l
        whites=[]
        # last=tiles[0][0]-1
        res=float("-inf")
        tw=0
        for each in tiles:
            # tb+=each[0]-last-1
            tw+=each[1]-each[0]+1
            whites.append(tw)
            # last=each[1]
        print(whites)
        for i in range(len(tiles)):
            c=0
            t=tiles[i][0]+carpetLen-1
            end=helper(t)
            # if(end>=len(tiles)):
            #     end=len(tiles)-1
            # if(tiles[end][0]<=t and t<=tiles[end][1]):
            #     # c=carpetLen-(blanks[end]-blanks[i])
            # elif(t<tiles[end][0] and tiles[end-1][1]<t):
            if(end>=len(tiles)):
                print("case 1")
                c+=whites[end-1]-(whites[i-1] if i-1>=0 else 0)
                res=max(res,c)
                continue
            if(tiles[end][0]<=t and t<=tiles[end][1]):
                print("case 2")
                c+=(whites[end-1] if end>0 else 0)-(whites[i-1] if i-1>=0 else 0)
                c+=t-tiles[end][0]+1
            elif(t<tiles[end][0] and tiles[end-1][1]<t):
                print("case 3")
                c+=whites[end-1]-(whites[i-1] if i-1>=0 else 0)
            elif(tiles[end-1][0]<t and t<=tiles[end-1][1]):
                print("case 4")
                c+=whites[end-2]-(whites[i-1] if i-1>=0 else 0)
                c+=t-tiles[end-1][0]+1
            print("*",i,end,c)
            res=max(res,c)
        return res









sol=Solution()
tiles = [[1,5],[10,11],[12,18],[20,25],[30,32]]
carpetLen = 10
# tiles = [[10,11],[1,1]]
# carpetLen = 2
tiles=[[1,1]]
carpetLen=1
print(sol.maximumWhiteTiles(tiles,carpetLen))