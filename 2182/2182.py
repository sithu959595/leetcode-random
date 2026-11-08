class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        uni=set()
        count={}
        for each in s:
            uni.add(each)
            count[each]=count.get(each,0)+1
        uni=list(uni)
        uni.sort(reverse=True)
        # print(uni)
        # print(max("a","b"))
        # print(count)
        res=[]
        c=0
        main=0
        filler=1
        # while(len(res)<len(s)):
        #     res.append(uni[main])
        #     count[uni[main]]-=1
        #     c+=1
        #     if(count[uni[main]]==0):
        #         while(not count[uni[main]]):
        #             main+=1
        #         if(main==len(uni)):
        #             break
        while(len(res)<len(s)):
            if(main==len(uni)-1):
                print("88",main)
                while(c!=repeatLimit and count[uni[main]]):
                    res.append(uni[main])
                    c+=1
                    count[uni[main]]-=1
                break
            res.append(uni[main])
            count[uni[main]]-=1
            print(main,res)
            c+=1
            if(count[uni[main]]==0):  #run out of count . take over filler
                if(filler==len(uni)):
                    break
                main=filler
                filler+=1
                c=0
                # if(res[-1]==uni[main]):
                #     c=1
            if(c==repeatLimit):       #hit limit
                if(filler>=len(uni)):
                    break
                res.append(uni[filler])
                count[uni[filler]]-=1
                c=0
                if(count[uni[filler]]==0):
                    # print("Hi")
                    filler+=1
            
        return "".join(res)
                




sol=Solution()
s = "cczazcc"
repeatLimit = 3

s = "aababab"
repeatLimit = 2

s = "ccbbba"
repeatLimit = 2
print(sol.repeatLimitedString(s,repeatLimit))