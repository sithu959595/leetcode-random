from collections import deque
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        # n=(str(left)[0])
        # nn=""
        # if(len(n)>1):
        #     for _ in range(len(str(left))-1):
        #         nn+=n
        # else:
        #     nn=left
        # print(nn)
        # q=deque()
        # # for j in range(jj,10,jj):
        # #     tem.add(j)
        # q.append(int(nn))
        res=[]
        def check(n):
            # print(n)
            d=[]
            nn=n
            while(n):
                # print(n)
                d.append(n%10)
                n=int(n/10)
            print(d)
            for each in d:
                if(each==0):
                    return False
                if(nn%each!=0):
                    return False
            return True
        for num in range(left,right+1):
            # if(num%10==0):
            #     continue
            if(check(num)):
                res.append(num)
        return res
        # while(q):


        # while(q):
        #     print(q)
        #     curQ=q.popleft()
        #     curS=s.popleft()
        #     for i in range(1,10):
        #         print("*",i)
        #         if(i in curS):
        #             cur=(curQ*10)+i
        #         t=set()
        #         ii=i
        #         while(ii<10):
        #             if(ii in curS):
        #                 t.add(ii)
        #             ii+=i
        #         if(cur<right):
        #             print(cur)
        #             s.append(t)
        #             q.append(cur)
        #         if(cur>=left and cur<=right):
        #             res.append(cur)
        # return res


sol=Solution()
left = 66
right = 708
print(sol.selfDividingNumbers(left,right))

# def check(n):
#             d=[]
#             nn=n
#             while(n):
#                 # print(n)
#                 d.append(n%10)
#                 n=int(n/10)
#             print(d)
#             for each in d:
#                 print(nn,each)
#                 if(nn%each!=0):
#                     return False
#             return True

# print(check(17))