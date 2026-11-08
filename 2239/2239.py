class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        smallest=nums[0]
        for i in range(1,len(nums)):
            cur=abs(nums[i])
            if(cur<abs(smallest)):
                smallest=nums[i]
            elif(cur==abs(smallest)):
                smallest=max(smallest,nums[i])
        return smallest