class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        if(len(s)==1):
            return 1
        res=0
        l,r=0,1
        exist=False
        start=None
        while(r<len(s)):
            if(s[r]==s[r-1] and exist):
                    res=max(res,(r-l))
                    l=start
                    exist=False
            if(s[r]==s[r-1] and not exist):
                    start=r
                    exist=True
            r+=1
        res=max(res,r-l)
        return res