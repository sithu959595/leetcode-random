class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        if(len(num)<3):
            return False
        def check(a,b):
            for i in range(len(a)):
                if(a[i]!=b[i]):
                    return False
            return True
        seq=[]
        def recur(p):
            nonlocal seq
            if(p>=len(num)):
                return True
            s=seq[-1]
            f=seq[-2]
            add=str(int(f)+int(s))
            if(add and num[p]=="0"):
                return False
            for l in range(len(add)):
                if(p>=len(num)):
                    return False
                if(num[p]!=add[l]):
                    return False
                p+=1
            seq.append(add)
            recur(p+1)
        for i in range(3,len(num)-1):
            partition=num[:i]
            for j in range(1,len(partition)):
                first=num[:j]
                second=num[j:len(partition)]
                # if(second[0]=="0"):
                #     continue
                seq=[first,second]
                if(recur(i)):
                    return True
        return False
            # seq=[]
                # add=int(first)+int(second)
                # k=len
                # seq=[first,second]
        
