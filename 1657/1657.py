class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        h1={}
        h2={}
        if(len(word1)!=len(word2)):
            return False
        for i in range(len(word1)):
            c1=word1[i]
            c2=word2[i]
            if(c1 not in h1):
                h1[c1]=0
            h1[c1]+=1
            if(c2 not in h2):
                h2[c2]=0
            h2[c2]+=1
        w1a=[]
        w1c=[]
        for j in h1:
            w1a.append(j)
            w1c.append(h1[j])
        w1a.sort()
        w1c.sort()
        w1a=tuple(w1a)
        w1c=tuple(w1c)
        w2a=[]
        w2c=[]
        for k in h2:
            w2a.append(k)
            w2c.append(h2[k])
        w2a.sort()
        w2c.sort()
        w2a=tuple(w2a)
        w2c=tuple(w2c)
        return (w1a==w2a and w1c==w2c)