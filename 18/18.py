class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        d=set()
        res=[]
        record=set()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                d=set()
                for k in range(len(nums)-1,j,-1):
                    three=nums[i]+nums[j]+nums[k]
                    find=target-three
                    # print("find",find,"fr",i,j,k)
                    if(find in d):
                        t=[nums[i],nums[j],nums[k],find]
                        t.sort()
                        t=tuple(t)
                        # print(t,record)
                        if(t not in record):
                            print("*")
                            res.append([nums[i],nums[j],nums[k],find])
                        record.add(t)
                    d.add(nums[k])
        return res


sol=Solution()
nums = [1,0,-1,0,-2,2]
target = 0
print(sol.fourSum(nums,target))