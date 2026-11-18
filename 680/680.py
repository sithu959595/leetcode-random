class Solution:
    def validPalindrome(self, s: str) -> bool:
        chance=True
        def recur(l,r):
            nonlocal chance
            if(l>=r):
                return True
            if(s[l]==s[r]):
                return recur(l+1,r-1)
            else:
                if(chance):
                    chance=False
                    return recur(l+1,r) or recur(l,r-1)
                else:
                    return False
        return recur(0,len(s)-1)

#