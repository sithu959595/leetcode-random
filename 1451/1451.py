# class Solution:
#     def arrangeWords(self, text: str) -> str:
#         s=text.split(" ")
#         re=[]
#         for i in range(len(s)):
#             cur=s[i].lower()
#             re.append([len(cur),i,cur])
#         re.sort()
#         res=[re[0][2].capitalize()]
#         for j in range(1,len(re)):
#             res.append(re[j][2])
#         return " ".join(res)

# sol=Solution()
# text = "Leetcode is cool"
# text = "Keep calm and code on"
# print(sol.arrangeWords(text))

a="aa"
# a[0]="b"
print(a[0])