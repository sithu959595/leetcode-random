class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        record={}
        cs=set()
        bulls=0
        cows=0

        #note digits from secret that are not bulls. note digits frm guess that are bulls so they cannot be cows.
        for i in range(len(guess)):
            if(guess[i]==secret[i]): #bulls
                cs.add(i)  #note digits frm guess that are bulls so they cannot be cows.
                bulls+=1
            else:
                record[secret[i]]=record.get(secret[i],0)+1    #note digits from secret that are not bulls.
        for j in range(len(guess)):
            if(j not in cs):
                if(guess[j] in record):
                    cows+=1
                    record[guess[j]]-=1
                    if(record[guess[j]]==0):
                        del record[guess[j]]