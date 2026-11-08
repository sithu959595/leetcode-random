class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        s=[]
        sToi={}
        total=0
        for i in range(len(nums)):
            total+=nums[i]
            s.append(total)
            sToi[total]=i

        print(s,total)
        res=float("inf")
        cur=0
        for j in range(len(nums)):
            l=total-s[j-1] if j!=0 else total
            cur=len(nums)-j
            print(j,"*******",l,cur,nums)
            if(l<target): #add repeat array
                req=target-l
                print("first",req)
                div=req//total
                rem=req%total
                cur+=len(nums)*div
                req-=total*div
                # while(req>total):
                #     print("---",cur)
                #     cur+=len(nums)
                #     req-=total
                print("new",cur,req)
                if(req==0):
                    res=min(res,cur)
                elif(req not in sToi):
                    cur=0
                    continue
                else:
                    print(cur,"---",sToi[req])
                    cur+=sToi[req]+1
            else:
                req=target+s[j-1] if j!=0 else target
                print("second",req)
                if(req not in sToi):
                    cur=0
                    continue
                else:
                    if(sToi[req]<j):
                        cur=0
                        continue
                    else:
                        cur=sToi[req]-j+1
                        print("&&&",cur)
            print("compare",res,cur)
            res=min(res,cur)
            cur=0
        return res if(res!=float("inf")) else -1


sol=Solution()
nums = [1,2,3]
target = 5

# nums = [1,1,1,2,3]
# target = 4

# nums = [2,4,6,8]
# target = 3

nums=[1,1,1]
target=1000000000

nums=[1,2,2,2,1,2,1,2,1,2,1]
target=83
nums=[2,5,6,4]
target=95
print(sol.minSizeSubarray(nums,target))