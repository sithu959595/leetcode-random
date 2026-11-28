class Solution:
    def calculateScore(self, s: str) -> int:
        h={}
        res=0
        for i in range(len(s)):
            frontD=ord(s[i])-ord("a")
            back=ord('z')-frontD
            find=chr(back)
            if(find in h):
                j=h[find][-1]
                res+=i-j
                h[find]=h[find][:-1]
                if(not h[find]):
                    del h[find]
            else:
                if(s[i] not in h):
                    h[s[i]]=[]
                h[s[i]].append(i)
        return res
