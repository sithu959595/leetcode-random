class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        tem=nums[:]
        whole=len(list(set(tem)))
        res=0
        for i in range(len(nums)):
            dis=set()
            for j in range(i, len(nums)):
                dis.add(nums[j])
                if(len(dis)==whole):
                    res+=1
                elif(len(dis)>whole):
                    break
                
        return res


sol=Solution()
nums=[1,3,1,2,2]
print(sol.countCompleteSubarrays(nums))