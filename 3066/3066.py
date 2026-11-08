import heapq
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        s=[]
        for each in nums:
            heapq.heappush(s,each)

        count=0
        while(True):
            if(s[0]>=k):
                return count
            count+=1
            one=heapq.heappop(s)
            two=heapq.heappop(s)
            heapq.heappush(s,(one*2)+two)

        