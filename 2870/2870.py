from collections import Counter 
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        c=Counter(nums)
        # print(c)
        res=0
        for each in c:
            cur=c[each]
            if(cur==1):
                return -1
            elif(cur%3==0):
                # print("*")
                res+=cur//3
            elif(cur%3==1):
                # print("**",cur//3)
                res+=(cur//3)-1
                res+=2
            elif(cur%3==2):
                # print("***",cur%3,cur)
                res+=cur//3
                res+=1
            # print(each,res)
        return res

sol=Solution()
nums = [2,3,3,2,2,4,2,3,4]
nums = [2,1,2,2,3,3]
nums=[1,1,1,1,1,1,1]
print(sol.minOperations(nums))