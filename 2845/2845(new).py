class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        lTr={}
        rTl={}
        cur=0
        count=[]
        for each in nums:
            if(each%modulo==k):
                count.append(1)
            else:
                count.append(0)
        for i in range(len(count)):
            if(count[i]==1):
                cur+=1
            # print(cur)
            lTr[cur]=lTr.get(cur,0)+1
            # lTr.append(cur)

        for j in range(len(count)-1,-1,-1):
            # rTl.append(cur)
            rTl[cur]=rTl.get(cur,0)+1
            if(count[j]==1):
                cur-=1
            print(cur)
        print(rTl)

sol=Solution()
nums = [3,2,4]
modulo = 2
k = 1

# nums = [3,1,9,6]
# modulo = 3
# k = 0
sol.countInterestingSubarrays(nums,modulo,k)