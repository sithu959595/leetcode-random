class Solution:
    def countPairs(self, nums: List[int]) -> int:
        def check(x,y):
            x=str(x)
            y=str(y)
            r=[]
            while(len(x)<len(y)):
                x="0"+x
            while(len(y)<len(x)):
                y="0"+y
            print(x,y)
            for i in range(len(x)):
                if(x[i]!=y[i]):
                    r.append(i)
            if(len(r)==0):
                return True
            elif(len(r)==2):
                first=r[0]
                second=r[1]
                if(x[first]==y[second] and y[first]==x[second]):
                    return True
                else:
                    return False
            else:
                return False
        res=0
        for j in range(len(nums)):
            for k in range(j+1,len(nums)):
                if(check(nums[j],nums[k])):
                    res+=1
        return res

sol=Solution()
nums = [100, 1]
print(sol.countPairs(nums))
