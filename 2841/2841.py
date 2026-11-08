# class Solution:
#     def maxSum(self, nums: List[int], m: int, k: int) -> int:
#         dist={}
#         curSum=0
#         res=0
#         l,r=0,0
#         while(r<len(nums)):
#             if(nums[r] in dist):
#                 dist[nums[r]]+=1
#             else:
#                 dist[nums[r]]=1
#             curSum+=nums[r]
#             if((r-l+1)<k):
#                 r+=1
#             else:
#                 if(len(dist)>=m):
#                     res=max(res,curSum)
#                 r+=1
#                 dist[nums[l]]-=1
#                 if(dist[nums[l]]==0):
#                     del dist[nums[l]]
#                 curSum-=nums[l]
#                 l+=1
#         return res

class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        dist={}
        curSum=0
        res=0
        l,r=0,0
        first=True
        while(r<len(nums)):
            # if(nums[r] in dist):
            #     dist[nums[r]]+=1
            # else:
            #     dist[nums[r]]=1
            # curSum+=nums[r]
            if((r-l)<k):
                print("h")
                if(nums[r] in dist):
                    dist[nums[r]]+=1
                else:
                    dist[nums[r]]=1
                curSum+=nums[r]
                r+=1
                if(len(dist)>=m):
                    res=max(res,curSum)
                # if((r-l+1)!=k): #normal
                #     r+=1
                # else:
                #     l-=1
            else:
                if(len(dist)>=m):
                    res=max(res,curSum)
                print(l,r,res)
                if(not first):
                    # print("add")
                    r+=1
                else:
                    first=False
                if(r>=len(nums)):
                    print("dfsd",dist)
                    break
                print(l,r)
                if(nums[r] in dist):
                    dist[nums[r]]+=1
                else:
                    dist[nums[r]]=1
                curSum+=nums[r]
                dist[nums[l]]-=1
                curSum-=nums[l]
                if(dist[nums[l]]==0):
                    del dist[nums[l]]
                l+=1
                if(len(dist)>=m):
                    res=max(res,curSum)
        return res

sol=Solution()
nums = [2,6,7,3,1,7]
m = 3
k = 4

# nums = [1]
# m = 1
# k = 1

# nums = [1,1,1]
# m = 1
# k = 1
print(sol.maxSum(nums,m,k))