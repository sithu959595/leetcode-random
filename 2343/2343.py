import heapq
class Solution:
    def smallestTrimmedNumbers(self, nums: list[str], queries: list[list[int]]) -> list[int]:
        h=[]
        res=[]
        LENGTH=len(nums[0])
        for query in queries:
            start=LENGTH-query[1]
            cur=""
            for j in range(len(nums)):
                heapq.heappush(h,[int(nums[j][start:]),j])
            for i in range(query[0]):
                cur=heapq.heappop(h)
            res.append(cur[1])
            h=[]
        return res
