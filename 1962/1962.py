import heapq
class Solution:
    def minStoneSum(self, piles: list[int], k: int) -> int:
        total=0
        arr=[]
        for each in piles:
            total+=each
            arr.append(-each)
        heapq.heapify(arr)
        for _ in range(k):
            if(not arr):
                print("hjjk")
                return total
            cur=-heapq.heappop(arr)
            sub=cur//2
            remain=cur-sub
            print(remain)
            if(remain):
                print("hi")
                heapq.heappush(arr,-remain)
            total-=sub
        return total
        

sol=Solution()
piles=[10000]
k=10000
print(sol.minStoneSum(piles,k))