class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(len(s)<2):
            return len(s)
        l,r=0,1
        res=0
        record=set()
        record.add(s[l])
        while(r<len(s)):
            if(s[r] in record):
                l=r
            else:
                res=max(res,r-l+1)
                record.add(s[r])
            r+=1
