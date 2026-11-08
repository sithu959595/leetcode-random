import math
class Solution:
    def minOperations(self, k: int) -> int:
        if(k==1):
            return 0
        d=2
        res=float("inf")
        while(True):
            indiv=math.ceil(k/d)
            tem=d-1
            tem+=indiv-1
            if(tem>res):
                return res
            else:
                res=tem
            d+=1


sol=Solution()
k = 11
print(sol.minOperations(k))