class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if(len(p)>len(s)):
            return []
        d={}
        res=[]
        cur={}
        def check(a,b):
            for key in a:
                if((key not in b) or (a[key]!=b[key])):
                    return False
            return True
        for each in p:
            d[each]=d.get(each,0)+1
        for j in range(len(p)):
            cur[s[j]]=cur.get(s[j],0)+1
        # if(check(d,cur)):
        #     res.append(0)
        start,end=0,len(p)-1
        while(end<len(s)):
            if(check(d,cur)):
                res.append(start)
            cur[s[start]]-=1
            if(cur[s[start]]==0):
                del cur[s[start]]
            start+=1
            end+=1
            if(end<len(s)):
                cur[s[end]]=cur.get(s[end],0)+1
            
        return res

sol=Solution()
s = "cbaebabacd"
p = "abc"
print(sol.findAnagrams(s,p))