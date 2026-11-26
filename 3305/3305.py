class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        l=r=0
        vowel={"a":0,"e":0,"i":0,"o":0,"u":0}
        def check():
            for each in vowel:
                if(vowel[each]==0):
                    return False
            return True
        curK=0
        res=0
        c=0
        while():
            while(not(check and curK==k)):
                if(word[r] in vowel):
                    vowel[word[r]]+=1
                else:
                    curK+=1
                r+=1
                if(r>=len(word)):
                    break  
            while(check and curK==k):
                if(word[r] in vowel):
                    vowel[word[r]]+=1
                else:
                    curK+=1
                r+=1
                c+=1
                if(r>=len(word)):
                    break  

        return res
        # while(l<len(word) or r<len(word)):
        #     if(word[r] in vowel):
        #         vowel[word[r]]+=1
        #     else:
        #         curK+=1
        #     while(curK>k):
        #         if(word[l] in vowel):
        #             vowel[word[l]]-=1
        #         else:
        #             curK-=1
        #         # if(curK==k and check()):
        #         #     res+=1
        #         l+=1
        #     if(curK==k and check()):
        #         tem=0
        #         while(curK==k):
        #             res+=1
        #             if(word[r] in vowel):
        #                 vowel[word[r]]+=1
        #             else:
        #                 curK+=1
        #         res-=1
        #     if(r<len(word)):
        #         r+=1
