from collections import heapq
class TimeMap:

    def __init__(self):
        self.record={}
    def bs(self,arr,target):
        l,r=0,len(arr)-1
        while(l<=r):
            m=(l+r)//2
            if(arr[m][0]==target):
                print("*",arr,target,arr[m][1])
                return arr[m][1]
            elif(target<arr[m][0]):
                r=m-1
            elif(arr[m][0]<target):
                l=m+1
        # if(l<0):
        #     return ""
        if(l>=len(arr)):
            print("**",arr,target,arr[-1][1])
            return arr[-1][1]
        elif(l==0):
            return ""
        else:
            print("***",arr,target,arr[l-1][1])
            return arr[l-1][1]


    def set(self, key: str, value: str, timestamp: int) -> None:
        if(key not in self.record):
            self.record[key]=[[timestamp,value]]
        else:
            self.record[key].append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
        if(key not in self.record):
            return ""
        # print(self.record[key])
        return self.bs(self.record[key],timestamp)


