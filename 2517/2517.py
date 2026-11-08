import heapq
class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        print(price)
        res=0
        tem=[]
        for i in range(1,len(price)): 
            # right=price[i+1] if i+1<len(price) else float("-inf")
            # left=price[i-1] if i-1>=0 else float("-inf")
            # res=(abs)
            print("*",i)
            # if(i+1<len(price)):
            #     print(abs(price[i+1]-price[i]))
            #     res=max(abs(price[i+1]-price[i]),res)
            # if(i-1>=0):
            #     print(abs(price[i-1]-price[i]))
            #     res=max(abs(price[i-1]-price[i]),res)
            tem.append(price[i]-price[i-1])
        print(tem)
        l=r=0
        res=tem[r]
        record={} #to delete
        cur=[]
        while(r<len(tem)):
            while(r-l+1<k):
                r+=1
                heapq.heappush(cur,tem[r])
                res=max(res,tem[r])
            record[tem[l]]=record.get(tem[l],0)+1
            l+=1
            while(cur[0] in record):
                record[cur[0]]-=1
                if(record[cur[0]]==0):
                    del record[cur[0]]
            r+=1
            if(r>=len(tem)):
                break
            heapq.heappush(cur,tem[r])
        return res


sol=Solution()
price = [34,116,83,15,150,56,69,42,26]
k = 6
print(sol.maximumTastiness(price,k))