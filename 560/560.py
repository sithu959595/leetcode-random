class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        h={}
        h[0]=1
        cur=0
        res=0
        for i in range(len(nums)):
            cur+=nums[i]
            find=cur-k
            res+=h.get(find,0)
            h[cur]=h.get(cur,0)+1
        return res


sol=Solution()
nums = [1,1,1]
k = 2
print(sol.subarraySum(nums,k))