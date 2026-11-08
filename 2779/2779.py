class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        res=0
        nums.sort()
        range=[None,nums[0]+k]
        l=r=0
        cur=0
        while(r<len(nums)):
            print(range)
            if(nums[r]-k<=range[1]): #add
                cur+=1
                res=max(res,cur)
                range=[nums[r]-k,range[1]]
                r+=1
            else:
                range[0]=nums[r]-k
                while(nums[l]+k<range[0]):
                    l+=1
                    cur-=1
                range[1]=nums[l]+k
                # l=r
                # range=[nums[l]-k,nums[l]+k]
                # cur=0
        return res

sol=Solution()
nums = [4,6,1,2]
k = 2

nums = [1,1,1,1]
k = 10
# nums=[48,93,96,19]
# k=24
print(sol.maximumBeauty(nums,k))
