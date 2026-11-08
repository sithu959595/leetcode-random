class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        sol=0
        def recur(point,sm,bg):
            nonlocal sol
            if(nums[point]<sm):
                sm=nums[point]
            if(bg<nums[point]):
                bg=nums[point]
            if((sm+bg)<=target):
                print(sm,bg)
                sol+=1
            i=point+1
            while(i<len(nums)):
                recur(i,sm,bg)
                i+=1
        # recur(-1,float('inf'),float('-inf'))
        for j in range(len(nums)):
            recur(j,float('inf'),float('-inf'))
        return sol

s=Solution()
# nums = [3,5,6,7]
# target = 9
nums = [3,3,6,8]
target = 10
# nums=[14,4,6,6,20,8,5,6,8,12,6,10,14,9,17,16,9,7,14,11,14,15,13,11,10,18,13,17,17,14,17,7,9,5,10,13,8,5,18,20,7,5,5,15,19,14]
# target=22
print(s.numSubseq(nums,target))