class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        dic={}
        res=float("inf")
        for i in range(len(cards)):
            if(cards[i] in dic):
                tem=i-dic[cards[i]]+1
                res=min(res,tem)
            dic[cards[i]]=i
        return res if res!=float("inf") else -1