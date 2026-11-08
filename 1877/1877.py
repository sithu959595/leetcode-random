class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        res=0
        for i in range(len(nums)/2):
            cur=nums[i]+nums[len(nums)-i-1]
            res=max(cur,res)
        return res