class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        d={}
        arr=[hours[i]%24 for i in range(len(hours))]
        print(arr)
        res=0
        for i in range(len(arr)):
            target=(24-arr[i])%24
            res+=0 if target not in d else d[target]
            d[arr[i]]=d.get(arr[i],0)+1
        return res

sol=Solution()
hours = [72,48,24,3]
print(sol.countCompleteDayPairs(hours))