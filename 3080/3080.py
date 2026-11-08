class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        s=[]
        total=0
        marked=set()
        for i in range(len(nums)):
            total+=nums[i]
            s.append([nums[i],i])
        s.sort()
        # oTn={s[j][1]:j for j in range(len(s))}
        res=[]
        p=0
        for k in range(len(queries)):
            cur=queries[k]
            if(cur[0] not in marked):
                total-=nums[cur[0]]
            marked.add(cur[0])
            for l in range(cur[1]):
                while(p<len(nums) and s[p][1] in marked):
                    p+=1
                if(p>=len(nums)):
                    break
                marked.add(s[p][1])
                total-=s[p][0]
            res.append(total)
        return res
            
