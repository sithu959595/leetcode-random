class Solution:
    def getDistances(self, arr: list[int]) -> list[int]:
        # d={}
        # res=[]
        # for i in range(len(arr)):
        #     c=d.get(arr[i],[])
        #     d[arr[i]]=c
        #     c.append(i)
        # for j in range(len(arr)):
        #     cur=0
        #     others=d[arr[j]]
        #     for each in others:
        #         cur+=abs(each-j)
        #     res.append(cur)
        # return res
        d={} #value:[total,count,lastIndex]
        res=[]
        lr=[0]*len(arr)
        for i in range(len(arr)):
            pre=d.get(arr[i],[0,0,None])
            preTotal=pre[0]
            preCount=pre[1]
            preLast=pre[2]
            dFLast=abs(preLast-i) if preLast!=None else 0
            cur=preTotal+(dFLast*preCount)
            print(arr[i],pre,preTotal,dFLast,preCount)
            d[arr[i]]=[cur,preCount+1,i]
            lr[i]=cur
        print("lr",lr)
        d={}
        rl=[0]*len(arr)
        for j in range(len(arr)-1,-1,-1):
            pre=d.get(arr[j],[0,0,None])
            preTotal=pre[0]
            preCount=pre[1]
            preLast=pre[2]
            dFLast=abs(preLast-j) if preLast else 0
            cur=preTotal+(dFLast*preCount)
            d[arr[j]]=[cur,preCount+1,j]
            rl[j]=cur
        print("rl",rl)
        for k in range(len(arr)):
            res.append(lr[k]+rl[k])
        return res
sol=Solution()
arr = [2,1,3,1,2,3,3]
# arr=[0,1,0,1,1,0,1,1]
print(sol.getDistances(arr))