class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s=set()
        taken=set()
        res=[]
        modify={}
        for i in range(len(strs)):
            c=strs[i]
            cc=list(c)
            cc.sort()
            ccc=str(cc)
            if(ccc not in modify):
                modify[ccc]=[i]
            else:
                modify[ccc].append(i)
        for cur in strs:
            if(cur in taken):
                continue
            scur=cur
            scur=list(scur)
            scur.sort()
            scur=str(scur)
            tem=[]
            for each in modify[scur]:
                taken.add(strs[each])
                tem.append(strs[each])
            res.append(tem)
            tem=[]
        return res
        # for each in strs:
        #     s.add(each)
        
        # for cur in strs:
        #     if(cur not in taken):
