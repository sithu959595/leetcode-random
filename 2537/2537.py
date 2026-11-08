class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        res=0
        past={}
        pairs=0
        l,r=0,-1
        while(r<len(nums)):
            # pairs+=past.get(nums[r],0)
            # past[nums[r]]=past.get(nums[r],0)+1
            if(pairs>=k):
                res+=1
                print("hi",l,r)
                res+=(len(nums)-1-r)
                pairs-=past[nums[l]]-1
                past[nums[l]]-=1
                l+=1
            else:
                r+=1
                if(r>=len(nums)):
                    break
                pairs+=past.get(nums[r],0)
                past[nums[r]]=past.get(nums[r],0)+1
        print(pairs)
        return res

sol=Solution()
nums = [3,1,4,3,2,2,4]
k = 2

# nums = [1,1,1,1,1]
# k = 10

print(sol.countGood(nums,k))