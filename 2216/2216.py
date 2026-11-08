# class Solution:
#     def minDeletion(self, nums: List[int]) -> int:
#         res=0
#         change=False
#         i=0
#         while(i<len(nums)):
#             if(not change): #normal
#                 if((i%2)==0):
#                     if((i+1)==len(nums)): #end
#                         res+=1
#                         return res
#                     elif(nums[i+1]==nums[i]):
#                         change=True
#                         i+=2
#                         res+=1
#                     elif(nums[i+1]!=nums[i]):
#                         i+=1
#                 else:
#                     i+=1
#             else: #changed before
#                 if((i%2)!=0):
#                     if((i+1)==len(nums)): #end
#                         res+=1
#                         return res
#                     elif(nums[i+1]==nums[i]):
#                         change=False
#                         i+=2
#                         res+=1
#                     elif(nums[i+1]!=nums[i]):
#                         i+=1
#                 else:
#                     i+=1
#         return res

class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        res=0
        i=0
        sub=0
        cur=nums[i]
        reali=0
        while(i<len(nums)):
            reali=i-sub
            if(reali%2==0): #even 
                cur=nums[i]
            else:       #odd 
                if(nums[i]==cur):
                    sub+=1
                    res+=1
            i+=1
        if((len(nums)-sub)%2!=0):
            res+=1
        return res