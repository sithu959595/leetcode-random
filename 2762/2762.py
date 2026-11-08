import heapq
class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        def helper(n):
            s=0
            for i in range(1,n+1):
                s+=i
            # print(":::",s)
            return s
        l=0
        res=0
        cur=0
        record={}
        smallest,greatest=float("inf"),float("-inf")
        for r in range(len(nums)):
            if nums[r] not in record:
                record[nums[r]]=r
            smallest=min(smallest,nums[r])
            greatest=max(greatest,nums[r])
            print(nums[r],"*",l,r,smallest,greatest,cur)
            if(greatest-smallest<=2):
                cur+=(r-l+1)
            else:
                print(cur,l,r)
                res+=cur
                cur=0
                tem=float("inf")
                s1=record.get(nums[r]-2,float("inf"))
                tem=min(tem,s1)
                s2=record.get(nums[r]-1,float("inf"))
                tem=min(tem,s2)
                e=record.get(nums[r],float("inf"))
                tem=min(tem,e)
                g1=record.get(nums[r]+2,float("inf"))
                tem=min(tem,g1)
                g2=record.get(nums[r]+1,float("inf"))
                tem=min(tem,g2)
            
                l=tem
                print("*******",l)
                smallest=min(nums[l],nums[r])
                greatest=max(nums[l],nums[r])
                cur=((r-l+1))
        return res+cur

sol=Solution()
nums = nums = [0, 3, 0]
print(sol.continuousSubarrays(nums))

