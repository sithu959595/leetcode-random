class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        avg=[0]*len(nums)
        i=0
        j=len(nums)-1
        while(i<len(nums) and i<k):
            avg[i]=-1
            i+=1
        while(j>=0 and j>=len(nums)-k):
            avg[j]=-1
            j-=1
        if(len(nums)<=(k*2)):
            return avg
        pre=[]
        tem=0
        # print(avg)
        for each in nums:
            tem+=each
            pre.append(tem)
        l=k
        while(l<len(nums) and avg[l]!=-1):
            leftEnd=l-k
            rightEnd=l+k
            cur=pre[rightEnd]-(pre[leftEnd-1] if leftEnd-1>=0 else 0)
            cur=cur/((k*2)+1)
            cur=int(cur)
            avg[l]=cur
            l+=1
        return avg


sol=Solution()
nums = [7,4,3,9,1,8,5,2,6]
k = 3

nums = [100000]
k = 0
print(sol.getAverages(nums,k))