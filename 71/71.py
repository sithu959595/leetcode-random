from collections import deque 
class Solution:
    def simplifyPath(self, path: str) -> str:
        a=path.split("/")
        stack=deque()
        for each in a:
            if(each):
                if(each=="."):
                    continue
                elif(each==".."):
                    if((stack)):
                        stack.pop()
                else:
                    stack.append(each)
        res="/".join(stack)
        return "/"+res

