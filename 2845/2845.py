class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        e=[0]
        for i in range(len(nums)):
            if(nums[i]%modulo==k):
                # print(nums[i])
                e.append(i)
        e.append(len(nums)-1)
        print(e)
        s=0
        ans=0
        for j in range(1,len(e)):
            if(j%modulo==k):
                print("***",e[j+1]-e[j]) 
                s+=1 if (e[j])==0 or e[j]==len(nums)-1 else e[j]-e[j-1]
                ans+=s*(e[j+1]-e[j]+1 if e[j]==0 or e[j]==len(nums)-1 else e[j+1]-e[j])
        return ans

sol=Solution()
nums = [3,2,4]
modulo = 2
k = 1

nums = [3,1,9,6]
modulo = 3
k = 0
print(sol.countInterestingSubarrays(nums,modulo,k))