class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        l=r=0
        s=nums[l]
        res=0
        while(r<len(nums)):
            if(s==k):
                if(r>=l):
                    res+=1
                r+=1
                if(r<len(nums)):
                    s+=nums[r]
            elif(s>k):
                while(s>k):
                    s-=nums[l]
                    l+=1
            else:
                r+=1
                if(r<len(nums)):
                    s+=nums[r]
        return res


sol=Solution()
nums = [1,1,1]
k = 2
print(sol.subarraySum(nums,k))