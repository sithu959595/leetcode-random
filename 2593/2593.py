class Solution:
    def findScore(self, nums: List[int]) -> int:
        score=0
        a=[(nums[i],i) for i in range(len(nums))]
        a.sort()
        # print(a)
        visited=set()
        while(a):
            cur=a.pop(0)
            if(cur[1] not in visited):
                visited.add(cur[1]-1)
                visited.add(cur[1])
                visited.add(cur[1]+1)
                score+=cur[0]
        return score

n=[2,4,1,2,5,2,3,6,7]
n=[2,1,3,4,5,2]
n=[2,3,5,1,3,2]
sol=Solution()
print(sol.findScore(n))