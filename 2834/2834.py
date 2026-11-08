class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        res=0
        s=set()
        cur=1
        i=1
        # for i in range(n):
        #     while(cur<target and target-cur in s):
        #         cur+=1
        #     res+=cur
        #     if(cur<target):
        #         s.add(cur)
        #     cur+=1
        #     # print(cur)
        # return res%((10**9)+7)
        # while(i<=n):
        #     print(cur)
        #     if(cur<target and cur>(target//2)):
        #         print("*",cur)
        #         cur=target
        #     res+=cur
        #     cur+=1
        #     i+=1
        first=target//2
        if((first)<n):
            res+=(first*(first+1))//2
        else:
            print("*")
            tem=(n*(n+1))//2
            tem=tem%((10**9)+7)
            return int(tem)
        print(res)
        a=(n-first-1)+target
        b=target-1
        print(a,b)
        second=((a*(a+1))//2)-(b*(b+1))//2
        res+=second
        res=res%((10**9)+7)
        return int(res)

sol=Solution()
n = 2
target = 3
n = 3
target = 3
print(sol.minimumPossibleSum(n,target))