class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        def helper(a,target):
            l,r=0,len(a)-1
            while(l<=r):
                m=(l+r)//2
                if(a[m]<target):
                    l=m+1
                else:
                    r=m-1
            return r
            
        lTr=[]
        rTl=[]
        pre=float("-inf")
        for i in range(len(arr)):
            if(arr[i]<pre):
                break   
            lTr.append(arr[i])
            pre=arr[i]
        if(len(lTr)==len(arr)):
            return 0
        pre=float('inf')
        for i in range(len(arr)-1,-1,-1):
            if(arr[i]>pre):
                break
            rTl=[arr[i]]+rTl[:]
            pre=arr[i]
        
        print(lTr,rTl)
        # if(len(lTr)==1 and lTr[0]>rTl[-1]):
        one=len(arr)-len(lTr)
        two=len(arr)-len(rTl)
        res=min(one,two)
        j=0
        while(j<len(lTr)):
            while(j+1<len(lTr) and lTr[j+1]==lTr[j]):
                j+=1
            tem=len(rTl)-helper(rTl,lTr[j])-1
            print((j+1),tem)
            total=(j+1)+tem
            res=min(res,len(arr)-total)
            j+=1
        return res


sol=Solution()
arr = [1,2,3,10,4,2,3,5]
arr = [5,4,3,2,1]
arr = [1,2,3]
arr=[33,28,36,28,9,9,24,37,16,20,2,38,37,9,39,19,34,16,0,7]
arr=arr = [1, 0, 0]
print(sol.findLengthOfShortestSubarray(arr))
