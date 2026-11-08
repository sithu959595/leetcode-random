class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        biggest=0
        res=0
        q=[]
        scaf=[-1 for _ in range(len(nums))]
        for each in nums:
            biggest=max(biggest,each)
        
        for i in range(len(nums)-1,-1,-1):
            if(nums[i]==biggest):
                q.append(i)
            if(len(q)>k):
                q.pop(0)
                scaf[i]=q[0]
            elif(len(q)==k):
                scaf[i]=q[0]
                # print("dfd",scaf)
        for j in range(len(nums)):
            s=scaf[j]
            if(s!=-1):
                res+=(len(nums)-scaf[j])
        # print(scaf)
        # print(res)
        return res

sol=Solution()
nums=[73,54,15,4,23,70,53,65,73,73,2,72,36,71,73,69,35,18,62,73,62,73,73,50,30,73,20,71,60,9,12,57,48,73,40,20,8,73,73,73,34,59,31,49,73,5,51,36,47,38,36,58,34,42,23,28,52,73]
# nums=[3, 1]
sol.countSubarrays(nums,1)