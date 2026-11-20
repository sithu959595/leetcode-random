class Solution:
    def countSubstrings(self, s: str) -> int:
        res=len(s)
        for i in range(len(s)):
            p=i+1
            for j in range(i+1,len(s)):
                if(s[j]==s[p-1]):
                    if(p-1)
                    res+=1
