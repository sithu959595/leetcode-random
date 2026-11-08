class Solution:
    def maximumWhiteTiles(self, tiles: list[list[int]], carpetLen: int) -> int:
        tiles.sort()
        res=float("-inf")
        for i in range(len(tiles)):
            cover=0
            cur=i
            # carpetleft=carpetLen+tiles[cur][0]-1
            carpetleft=carpetLen
            last=tiles[i][0]-1
            while(cur<len(tiles)):
                print("--",last)
                print("blank",min(carpetleft,tiles[cur][0]-last-1))
                carpetleft-=min(carpetleft,tiles[cur][0]-last-1)
                if(not carpetleft): #no more carpet
                    break
                print("cover",min(carpetleft,(tiles[cur][1]-tiles[cur][0]+1)))
                cover+=min(carpetleft,(tiles[cur][1]-tiles[cur][0]+1))
                print("while",min(carpetleft,(tiles[cur][1]-tiles[cur][0]+1)))
                carpetleft-=min(carpetleft,(tiles[cur][1]-tiles[cur][0]+1))
                if(not carpetleft): #no more carpet
                    break
                last=tiles[cur][1]
                cur+=1
            print("*",i,cover)
            res=max(res,cover)
        return res

sol=Solution()
tiles = [[1,5],[10,11],[12,18],[20,25],[30,32]]
carpetLen = 10
tiles = [[10,11],[1,1]]
carpetLen = 2
print(sol.maximumWhiteTiles(tiles,carpetLen))