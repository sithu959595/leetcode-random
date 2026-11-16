class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        if(len(num)<3):
            return False
        # def check(a,b):
        #     for i in range(len(a)):
        #         if(a[i]!=b[i]):
        #             return False
        #     return True
        seq=[]
        def recur(p):
            nonlocal seq
            if(p>=len(num)):
                print("TTTTTTTTTTT",seq)
                return True
            s=seq[-1]
            f=seq[-2]
            add=str(int(f)+int(s))
            print("^^",seq,add,p)
            if(int(add) and num[p]=="0"):
                print("zero",add,num)
                return False
            for l in range(len(add)):
                if(p>=len(num)):
                    print("***")
                    return False
                if(num[p]!=add[l]):
                    print("(((((((((((())))))))))))",p,add)
                    return False
                p+=1
            seq.append(add)
            return recur(p)
        for i in range(2,len(num)):
            partition=num[:i]
            print("*",partition)
            for j in range(1,len(partition)):
                first=num[:j]
                if(first[0]=="0" and len(first)>1):
                    continue
                second=num[j:len(partition)]
                if(second[0]=="0" and len(second)>1):
                    continue
                seq=[first,second]
                print("$$",seq)
                if(recur(i)):
                    print("Doneeee")
                    return True
        return False
            # seq=[]
                # add=int(first)+int(second)
                # k=len
                # seq=[first,second]
        

sol=Solution()
num="112358"
num="123"
num="000"
num="011112"
print(sol.isAdditiveNumber(num))