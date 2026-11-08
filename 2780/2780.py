from collections import Counter
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        count=Counter(nums)
        d=0
        t=0
        for each in count:
            if(count[each]>t):
                t=count[each]
                d=each
        print(d)
        arr=[]
        curD=0
        for i in range(len(nums)):
            if(nums[i]==d):
                curD+=1
            arr.append(curD)
        print(arr)
        for j in range(len(nums)):
            firstLen=j+1
            first=arr[j]
            secondLen=len(arr)-j-1
            second=arr[-1]-arr[j]
            print(j,first,firstLen,second,secondLen)
            if((2*first)>firstLen and (2*second)>secondLen):
                return j
        return -1

sol=Solution()
nums = [1,2,2,2]
print(sol.minimumIndex(nums))