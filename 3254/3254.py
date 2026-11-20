class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if(len(nums)<2):
            return nums
        res=[]
        l=r=0
        while(r<len(nums)): #3,2
            if(l==r or nums[r-1]+1==nums[r]):     #2,3
                curl=r-l+1
                if(curl==k):
                    res.append(nums[r])
                    l+=1
                r+=1
            else: #3,2


            if(nums[r-1]+1!=nums[r]):
                while(l!=r):
                    if(l+k-1<len(nums)):
                        res.append(-1)
                    l+=1
                r+=1
            else:  #2,3
                curl=r-l+1
                if(curl==k):
                    res.append(nums[r])
                    l+=1
                r+=1
        return res