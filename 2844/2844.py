# class Solution:
#     def minimumOperations(self, num: str) -> int:
#         res=float("inf")
#         def recur(cur,n):
#             # print("*",n,cur)
#             nonlocal res
#             if(n=="" or int(n)%25==0):
#                 # print("**",n)
#                 res=min(res,len(num)-len(n))
#             if(cur<0):
#                 return
#             if(n and (n[-1]!="0" and n[-1]!="5")):
#                 return
#             recur(cur-1,num[cur]+n)
#             recur(cur-1,n)
#         recur(len(num)-1,"")
#         return res

class Solution:
    def minimumOperations(self, num: str) -> int:
      if(int(num)==0):
        return 0
      record={"0":-1}
      record[num[0]]=0
      res=len(num)
      for i in range(1,len(num)):
        cur=num[i]
        print(i,cur)
        print(record)
        if(cur=="0"):
            zero=float("-inf")
            five=float("-inf")
            if("0" not in record and "5" not in record):
                record[cur]=i
                continue
            if("0" in record):
                zero=record["0"]
            if("5" in record):
                # print("*")
                five=record["5"]
            before=max(zero,five)
            dis=i-before-1+(len(num)-i-1)
            res=min(res,dis)
        elif(cur=="5"):
            two=float("-inf")
            seven=float("-inf")
            if("2" not in record and "7" not in record):
                record[cur]=i
                continue
            if("2" in record):
                two=record["2"]
            if("7" in record):
                # print("*")
                seven=record["7"]
            before=max(two,seven)
            dis=i-before-1+(len(num)-i-1)
            res=min(res,dis)
            # if("2" not in record):
            #     record[cur]=i
            #     continue
            # two=record["2"]
            # before=two
            # dis=i-before-1+(len(num)-i-1)
            # res=min(res,dis)
        record[cur]=i
      return res
    
            


sol=Solution()
# num = "10"
num="50"
num = "2245047"
num = "2908305"
# num="5079348434341304786187138148710190664"
print(sol.minimumOperations(num))

# n="0"
# if(n=="" or int(n)%25==0):
#     print("*",n)

