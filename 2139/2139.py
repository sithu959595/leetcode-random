class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        res=0
        while(target!=1):
            if(maxDoubles):
                if((target%2)!=0):
                    print("not dividable")
                    res+=1
                    target-=1
                    continue
                print("double")
                maxDoubles-=1
                target/=2
                res+=1
            else:
                print("minux")
                res+=(target-1)
                target=1
        return int(res)


sol=Solution()
target = 19
maxDoubles = 2

# target = 5
# maxDoubles = 0
print(sol.minMoves(target,maxDoubles))