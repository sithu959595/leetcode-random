class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        while(l<=r):
            print(l,r)
            m=(l+r)//2
            if(target==nums[m]):
                return m
            if(nums[m]<nums[r]):
                if(nums[m]<target and target<=nums[r]):
                    l=m+1
                else:
                    r=m-1
            elif(nums[l]<=nums[m]):
                if(nums[l]<=target and target<nums[m]):
                    r=m-1
                else:
                    l=m+1
        return -1

sol=Solution()
nums = [4,5,6,7,0,1,2]
target = 0
nums = [4,5,6,7,0,1,2]
target = 3
print(sol.search(nums,target))