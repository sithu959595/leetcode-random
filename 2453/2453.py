class Solution:
    def destroyTargets(self, nums: list[int], space: int) -> int:
        record={} #remainder:(count,nums[i])
        for each in nums:
            remainder=each%space
            tem=record.get(remainder,[0,float("inf")])
            tem[0]=tem[0]+1
            tem[1]=min(tem[1],each)
            record[remainder]=tem
        res=[float("-inf"),float("inf")]
        for each in record:
            if(record[each][0]>res[0]):
                res=record[each]
            elif(record[each][0]==res[0]):
                if(record[each][1]<res[1]):
                    res=record[each]
        return res[1]

sol=Solution()
nums = [3,7,8,1,1,5]
space = 2

nums = [1,3,5,2,4,6]
space = 2
nums = [1, 2, 4]
space = 2
print(sol.destroyTargets(nums,space))