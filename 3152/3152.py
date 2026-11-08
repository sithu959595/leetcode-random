class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        count=[0]
        pre=nums[0]
        cc=count[0]
        isPreEven=(pre%2)==0
        for i in range(1,len(nums)):
            cur=nums[i]
            if(isPreEven):    #pre is even
                if(cur%2==0): #even again. not special
                    cc+=1
                    count.append(cc)
                else:     #still special
                    count.append(cc)
            else:        #pre is odd
                if(cur%2==0):    #even. still speical
                    count.append(cc)
                else: #odd again. not special.
                    cc+=1
                    count.append(cc)
            isPreEven=(cur%2)==0
        print(count)
        res=[]
        for q in queries:
            tem=count[q[1]]-count[q[0]]
            if(tem):
                res.append(False)
            else:
                res.append(True)
        return res


sol=Solution()
nums = [3,4,1,2,6]
queries = [[0,4]]

# nums = [4,3,1,6]
# queries = [[0,2],[2,3]]
print(sol.isArraySpecial(nums,queries))