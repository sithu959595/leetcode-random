class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def recur(cur,s):
            if(cur>=len(nums)):
                res.append(s)
                return
            
            recur(cur+1,s)
            recur(cur+1,s+[nums[cur]])
        recur(0,[])
        return res