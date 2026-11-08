class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        # r=[int(str(each)[::-1]) for each in nums]
        re={}
        ans=0
        MOD = 10**9 + 7
        for i in range(len(nums)-1,-1,-1):
            curre=int(str(nums[i])[::-1])
            find=(nums[i]-curre)
            ans+=re[find] if find in re else 0

            if(find not in re):
                re[find]=1
            else:
                re[find]+=1
        return ans%MOD
