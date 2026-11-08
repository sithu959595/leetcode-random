class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        p1,p2=0,0
        while(p1<len(version1) or p2<len(version2)):
            num1=""
            num2=""
            tem=""
            if(p1<len(version1)):
                while(p1!=len(version1) and version1[p1]!="."):
                    tem+=version1[p1]
                    p1+=1
                num1=int(tem)
                tem=""
                p1+=1
            else:
                num1=0
            if(p2<len(version2)):
                while(p2!=len(version2) and version2[p2]!="."):
                    tem+=version2[p2]
                    p2+=1
                num2=int(tem)
                tem=""
                p2+=1
            else:
                num2=0
            if(num1<num2):
                return -1
            elif(num1>num2):
                return 1
        return 0
        # num1=[]
        # num2=[]
        # tem=""
        # for each in version1:
        #     if(each=="."):
        #         num1.append(tem)
        #         tem=""
        #     else:
        #         tem+=each
# a="1"
# b="2"
# c=a+b
# print(c)
# a="abc"
# for i in a:
#     print(i)

sol=Solution()
version1 = "1.2"
version2 = "1.10"
version1 = "1.01"
version2 = "1.001"
version1 = "1.0"
version2 = "1.0.0.0"
print(sol.compareVersion(version1,version2))