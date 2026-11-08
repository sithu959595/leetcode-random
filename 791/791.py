class Solution:
    def customSortString(self, order: str, s: str) -> str:
        taken=set()
        record={order[i]:i for i in range(len(order))}
        size=len(s)
        t={order[i]:0 for i in range(len(order))}
        for j in range(len(s)):
            if(s[j] in record):
                taken.add(j)
                t[s[j]]+=1
        res=""
        for each in t:
            for k in range(t[each]):
                res+=each
        def recur(cur):
            if(len(taken)==size):
                return cur
            for j in range(len(s)):
                if(j in taken):
                    continue
                print(cur,s[j])
                # if(s[j] in record):
                #     if(record[s[j]]<last):
                #         print("here")
                #         return None
                #     else:
                #         taken.add(j)
                #         tem=recur(cur+s[j],record[s[j]])
                #         taken.remove(j)
                taken.add(j)
                tem=recur(cur+s[j])
                taken.remove(j)
                if(tem):
                    return tem  
        # print(res)
        return recur(res)

        # def recur(cur,last):
        #     if(len(taken)==size):
        #         return cur
        #     for j in range(len(s)):
        #         if(j in taken):
        #             continue
        #         print(cur,s[j])
        #         if(s[j] in record):
        #             if(record[s[j]]<last):
        #                 print("here")
        #                 return None
        #             else:
        #                 taken.add(j)
        #                 tem=recur(cur+s[j],record[s[j]])
        #                 taken.remove(j)
        #         else:
        #             taken.add(j)
        #             tem=recur(cur+s[j],last)
        #             taken.remove(j)
        #         if(tem):
        #             return tem 
        # return recur("",-1)

sol=Solution()
order = "cba"
s = "abcd"
order = "bcafg"
s = "abcd"
order = "kqep"
s = "pekeq"
print("***",sol.customSortString(order,s))