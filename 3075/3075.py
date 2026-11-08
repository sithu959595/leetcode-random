class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        sub=0
        res=0
        index=len(happiness)-1
        happiness.sort()
        for i in range(k):
            res+=0 if (happiness[index]-sub)<0 else happiness[index]-sub
            sub+=1
            index-=1
        return res