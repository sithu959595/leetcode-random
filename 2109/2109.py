class Solution:
    def addSpaces(self, s: str, spaces: list[int]) -> str:
        curSpace=0
        res=[]
        for i in range(len(s)):
            if(curSpace<len(spaces) and i==spaces[curSpace]):
                print("*")
                curSpace+=1
                res.append(" ")
                res.append(s[i])
            else:
                res.append(s[i])
            # print(res)
        return "".join(res)

sol=Solution()
s = "LeetcodeHelpsMeLearn"
spaces = [8,13,15]

s = "icodeinpython"
spaces = [1,5,7,9]
print(sol.addSpaces(s,spaces))