class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        a=[True for _ in range(n)]
        cur=0
        pre=0
        for _ in range(n-1):
            # print("h")
            for _ in range(k):
                pre=cur
                cur=(cur+1)%n
                while(not a[cur]):
                    cur=(cur+1)%n
            a[pre]=False
            print(a,pre,cur)
        # print(a)
        while(not a[cur]):
            cur=(cur+1)%n
        return cur+1

sol=Solution()
print(sol.findTheWinner(6,5))