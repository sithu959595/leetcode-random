class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        b=set()
        for each in bank:
            b.add(each)
        visited=set()
        q=[startGene]
        nq=[]
        cur=startGene
        possible=["A","C","G","T"]
        res=0
        s=0
        while(True):
            res+=1
            e=(len(q))
            for j in range(s,e):
                cur=q[j]
                print(q)
                for i in range(len(cur)): #change each character
                    for replace in possible: 
                        if(replace!=cur[i]):
                            edit=cur[0:i]+replace+cur[i+1:]
                            print(edit)
                            if(edit in bank and edit not in visited):
                                if(edit==endGene):
                                    return res
                                visited.add(edit)
                                q.append(edit)
            s=e
            print(q,s)
            # print(nq)
            # if(not nq):
            #     return -1
            if(len(q)<=s):
                return -1
            # q=nq[:]
            # nq=[]

sol=Solution()

startGene = "AAAA"
endGene = "AACC"
bank = ["CAAA", "AAAC", "AACC"]
startGene = "AAA"
endGene = "ACC"
bank = ["AAC", "ACC"]
print(sol.minMutation(startGene,endGene,bank))