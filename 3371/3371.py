class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        s=0
        h={}
        res=0
        for i in range(len(nums)):
            s+=nums[i]
            if(nums[i] not in h):
                h[nums[i]]=set()
            h[nums[i]].add(i)
            
        for j in range(len(nums)):
            cur=nums[j]
            remain=s-cur
            find=remain-cur
            if(find in h):
                outlier=h[find]
                if(not(len(outlier)==1 and j in outlier)): #not valid outlier
                    res=max(res,find)
        return res

