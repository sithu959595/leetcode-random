class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        ss=[]
        for i in range(len(s)):
            if((ord(s[i])>=ord("a") and ord(s[i])<=ord("z")) or (ord("0")<=ord(s[i]) and ord("9")>=ord(s[i]))):
                ss.append(s[i])
        l,r=0,len(ss)-1
        while(l<=r):
            if(ss[l]!=ss[r]):
                return False
            l+=1
            r-=1
        return True

