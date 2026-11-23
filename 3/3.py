class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(len(s)<2):
            return len(s)
        l,r=0,1
        res=1
        record={}
        record[s[l]]=l
        while(r<len(s)):
            if(s[r] in record): #invalid
                l=record[s[r]]+1
                r=l
                record={}
                record[s[l]]=l
            else:
                res=max(res,r-l+1)
                record[s[r]]=r
            r+=1
        return res
