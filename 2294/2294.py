class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        res=0
        record=[]
        nums.sort()
        cura=[nums[0]]
        i=1
        start=nums[0]
        while(i<len(nums)):
            print(cura,record)
            if(nums[i]-start<=k):
                cura.append(nums[i])
                i+=1
            else:
                start=nums[i]
                record.append(cura)
                cura=[start]
                i+=1
                res+=1
        if(nums[-1]-start<=k):
            res+=1
        return res
        # tem=[]
        # mem=set()
        # for each in nums:
        #     if(each not in mem):
        #         tem.append(each)
        #         mem.add(each)
        # nums=tem[:]
        # res=0
        # taken=set()
        # smallest,greatest=float("inf"),float("-inf")
        # count=0
        # while(count<len(nums)):
        #     print(count,taken)
        #     i=0
        #     smallest,greatest=float("inf"),float("-inf")
        #     while(i<len(nums)):
        #         if(nums[i] in taken):
        #             i+=1
        #             continue
        #         temS,temG=smallest,greatest
        #         smallest=min(smallest,nums[i])
        #         greatest=max(greatest,nums[i])
        #         diff=greatest-smallest
        #         if(diff<=k): #put in the current sub.
        #             count+=1
        #             taken.add(nums[i])
        #             i+=1
        #         else: #do not put in the current sub.Reset smallest and greatest. Skip.
        #             # print("***",taken,smallest,greatest)
        #             smallest,greatest=temS,temG
        #             i+=1
        #     print("**",taken)
        #     res+=1
        # print(taken)
        # return res
        # # for each in nums:
        # #     smallest=min(smallest,each)
        # #     greatest=max(greatest,each)
        # #     diff=greatest-smallest
        # #     if(diff>k):
        # #         res+=1
        # #         smallest,greatest=float("inf"),float("-inf")

sol=Solution()
nums = [3,6,1,2,5]
k = 2
nums = [1,2,3]
k = 1

nums = [2,2,4,5]
k = 0

nums =[16,8,17,0,3,17,8,20]
k=10
print(sol.partitionArray(nums,k))