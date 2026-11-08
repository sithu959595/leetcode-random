class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        res=[]
        nums.sort()
        for i in range(int(len(nums)/3)):
            r=[]
            startI=i*3
            lastI=(i*3)+2
            last=nums[lastI]
            print("*",startI,lastI)
            for j in range(startI,startI+3):
                print(i,j)
                if(last-nums[j]>k):
                    # print("*")
                    return []
                r.append(nums[j])
            res.append(r)
        return res

sol=Solution()
nums = [1,3,4,8,7,9,3,5,1]
k = 2
print(sol.divideArray(nums,k))