class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        i=0
        s=0
        for each in chalk:
            s+=each
        k=k%s
        while(True):
            if(k<chalk[i]):
                return i
            k-=chalk[i]
            i=(i+1)%len(chalk)
