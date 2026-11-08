class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        colors=[0]*n
        adj=0

        ans=[]
        for each in queries:
            left=0 if each[0]-1<0 else colors[each[0]-1]
            right=0 if each[0]+1>=len(colors) else colors[each[0]+1]
            print(left,right)
            if(colors[each[0]]):
                print("sub")
                if(left and left==colors[each[0]]):
                    adj-=1
                if(right and right==colors[each[0]]):
                    adj-=1
            colors[each[0]]=each[1]
            # print("*",left,colors[left],colors[each[0]])
            if(left and left==colors[each[0]]):
                # print("add for left")
                adj+=1
            if(right and right==colors[each[0]]):
                # print("add for right")
                adj+=1
            ans.append(adj)
            # print(colors,ans)
        return ans


sol=Solution()
n = 4
queries = [[0,2],[1,2],[3,1],[1,1],[2,1]]
print(sol.colorTheArray(n,queries))