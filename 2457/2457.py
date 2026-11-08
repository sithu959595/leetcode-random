class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        def helper(num):
            res=0
            while(num):
                res+=(num%10)
                num//=10
            return res
        x=0
        d=10
        if(helper(n)<=target):
            return x
        while(helper(n+x)>target):
            cur=n%d
            x=(((cur//d)+1)*d)-cur
            d*=10
        return x


sol=Solution()
print(sol.makeIntegerBeautiful(1,1))
# print(385%100)