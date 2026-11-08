class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        incomplete={}
        complete={}
        l=r=0
        res=0
        while(r<len(nums)):
            if(nums[r] not in complete):
                complete[nums[r]]=1
            else:
                complete[nums[r]]+=1
            if(complete[nums[r]]>k):
                while(complete[nums[r]]!=k):
                    print(complete)
                    complete[nums[l]]-=1
                    l+=1
            else:
                res=max(res,(r-l+1))
            r+=1
        return res

sol=Solution()
nums = [1,2,3,1,2,3,1,2]
k = 2
print(sol.maxSubarrayLength(nums,k))