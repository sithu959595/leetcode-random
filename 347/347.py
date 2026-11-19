import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h=[]
        d={}
        for i in range(len(nums)):
            d[nums[i]]=d.get(nums[i],0)+1
        for key in d:
            h.append([-d[key],key])
        heapq.heapify(h)
        res=[]
        for _ in range(k):
            cur=heapq.heappop(h)
            res.append(cur[1])
        return res