class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        pre=float("inf")
        res=cur=0
        length=[0]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            if(nums[i]<pre): #strictly increase
                cur+=1
                pre=nums[i]
                length[i]=cur
            else:
                pre=nums[i]
                length[i]=1
                cur=1
            # if(i+cur<len(nums)):
            #     tem=length[i+cur]
            #     tem=min(tem,cur)
            #     print(i,cur,tem)
            #     res=max(res,tem)

        pre=float("-inf")
        cur=0
        for j in range(len(nums)):
            if(nums[j]>pre): #strictly increase
                print("increase","at",j,pre,cur)
                cur+=1
                pre=nums[j]
            else:
                print("not increase","at",j,pre,cur)
                cur=1
                pre=nums[j]
            print(cur,res)
            if((j+1)<len(nums)):
                tem=min(length[j+1],cur)
                res=max(res,tem)
                print("*",j,res)
            
        print(length)
        return res

sol=Solution()
nums = [2,5,7,8,9,2,3,4,3,1]
nums = [1,2,3,4,4,4,4,5,6,7]
print(sol.maxIncreasingSubarrays(nums))