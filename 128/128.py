class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        taken=set()
        res=0
        d=set()
        for e in nums:
            d.add(e)
        for each in nums:
            if(each in taken):
                continue
            #greater
            n=each
            n=n+1
            r=1
            while(n in d):
                r+=1
                taken.add(n)
                n+=1
            #smaller
            n=each
            n-=1
            while(n in d):
                r+=1
                taken.add(n)
                n-=1
            res=max(res,r)
        return res