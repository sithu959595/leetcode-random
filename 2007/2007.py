class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if(len(changed)%2!=0):
            return []
        changed.sort()
        c={}
        taken=[False]*len(changed)
        ans=[]
        for i in range(len(changed)):
            if(changed[i] not in c):
                c[changed[i]]=[]
            c[changed[i]].append(i)
        for j in range(len(changed)):
            if(taken[j]):
                continue
            twice=changed[j]*2
            if(twice in c and c[twice]):
                ii=c[twice].pop()
                taken[ii]=True
                ans.append(changed[j])
            else:
                return []
        return ans
