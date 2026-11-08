class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        def bs(target,l,r,arr):
            while(l<=r):
                m=(l+r)//2
                if(arr[m]<=target):
                    l=m+1
                else:
                    r=m-1
            return l
        t=0
        res=-1
        arr=[]
        for each in nums:
            t+=each
            arr.append(t)
        print(arr)
        for i in range(1,len(arr)):
            # if(nums[i]<arr[i-1]):
                # res=max(res,arr[i])
            cut=bs(nums[i],0,i-1,arr)
            print(nums[i],cut)
            if(cut and nums[i]<arr[cut-1]):
                print("*",nums[i])
                res=max(res,arr[i])
        return res
        
sol=Solution()
nums = [1,12,1,2,5,50,3]
print(sol.largestPerimeter(nums))
