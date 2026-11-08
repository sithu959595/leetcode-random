class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        res=[]
        dic={nums[i]:-1 for i in range(len(nums))}
        for j in range(len(nums)):
            cur=nums[j]
            target=dic[cur]+1
            if(len(res)<target+1):
                res.append([])
            dic[cur]=target
            res[target].append(cur)
        return res


sol=Solution()
nums = [1,3,4,1,2,3,1]
print(sol.findMatrix(nums))