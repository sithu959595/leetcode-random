class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        a1=[]
        a2=[]
        for each in arr1:
            a1.append(str(each))
        for each in arr2:
            a2.append(str(each))
        arr1=a1
        arr2=a2
        arr1.sort()
        d={}
        res=0
        for i in range(len(arr1)):
            if(arr1[i][0] not in d):
                d[arr1[i][0]]=i
        # print(arr1)
        # print(d)
        for two in arr2:
            if(len(two)<res):
                continue
            if(two[0] not in d):
                continue
            j=d[two[0]]
            k=0
            o=t=0
            while(j<len(arr1) and t<len(two)):
                if(o>=len(arr1[j])):
                    # if(j+1<len(arr1) and arr[1][j+1])
                    break
                if(arr1[j][:o+1]==two[:t+1]):
                    # print(j,o,t,arr1[j][:o+1],two[:t+1])
                    while(o+1<len(arr1[j]) and t+1<len(two) and arr1[j][o+1]==two[t+1]):
                        o+=1
                        t+=1
                    res=max(res,t+1)
                    j+=1
                    # o+=1
                    # t+=1
                else:
                    break
                    # if(int(arr1[j][o])<int(two[t])):
                    #     j+=1
                    # elif(int(arr1[j][o])>int(two[t])):
                    #     break
        return res


sol=Solution()
arr1 = [1,10,100]
arr2 = [1000]
print(sol.longestCommonPrefix(arr1,arr2))
