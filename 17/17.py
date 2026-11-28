class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        m={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        res=[]
        def recur(p,s):
            if(p>=len(digits)):
                res.append(s)
                return
            cur=digits[p]
            avail=m[cur]
            for each in avail:
                recur(p+1,s+each)
        recur(0,"")
        return res
