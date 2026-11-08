class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos=[]
        neg=[]
        for i in range(len(nums)):
            if(nums[i]>0):
                pos.append(nums[i])
            else:
                neg.append(nums[i])
        res=[]
        res.append(pos.pop(0))
        while(pos or neg):
            if(res[-1]>0):
                res.append(neg.pop(0))
            else:
                res.append(pos.pop(0))
        return res
