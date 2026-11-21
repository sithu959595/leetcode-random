class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        toRight=[1]*len(nums)
        toLeft=[1]*len(nums)
        cur=1
        # for i in range(len(nums)):
        #     cur=cur*nums[i]
        #     toRight.append(cur)
        # cur=1
        for j in range(len(nums)-1,-1,-1):
            cur=cur*nums[j]
            toLeft[j]=cur
        cur=1
        res=[]
        for i in range(len(nums)):
            front=1 if i==0 else toRight[i-1]
            back=1 if i==len(nums)-1 else toLeft[i+1]
            cur=cur*nums[i]
            toRight[i]=cur
            tem=front*back
            res.append(tem)
        return res