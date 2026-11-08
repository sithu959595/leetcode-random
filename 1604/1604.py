from collections import deque
class Solution:
    def alertNames(self, keyName: list[str], keyTime: list[str]) -> list[str]:
        k=[]
        for i in range(len(keyName)):
            t=keyTime[i]
            h=int(t[0:2])
            m=int(t[3:6])
            k.append([keyName[i],h,m])
        k.sort()
        # print(k)
        def inOne(left,right):
            h=(left[1]+1)%24
            if(h==0):
                h=24
            m=left[2]
            print("enter",h,m,left,right)
            if(right[1]<h):
                # print("top",left,right)
                return True
            elif(right[1]==h):
                # print("b",left,right)
                return right[2]<=m


        res=[]
        record={}
        for j in range(len(k)):
            if(k[j][0] not in record):
                # print(j)
                record[k[j][0]]=deque([k[j]])
            else:
                if(len(record[k[j][0]])>=3):
                    continue
                while(record[k[j][0]] and not inOne(record[k[j][0]][0],k[j])):
                    record[k[j][0]].popleft()
                record[k[j][0]].append(k[j])
                if(len(record[k[j][0]])>=3):
                    res.append(k[j][0])
            # print(record)
        return res


sol=Solution()
keyName = ["daniel","daniel","daniel","luis","luis","luis","luis"]
keyTime = ["10:00","10:40","11:00","09:00","11:00","13:00","15:00"]

keyName = ["alice","alice","alice","bob","bob","bob","bob"]
keyTime = ["12:01","12:00","18:00","21:00","21:20","21:30","23:00"]

keyName=["a","a","a","a","a","b","b","b","b","b","b"]
keyTime=["23:20","11:09","23:30","23:02","15:28","22:57","23:40","03:43","21:55","20:38","00:19"]
print(sol.alertNames(keyName,keyTime))
                
            
