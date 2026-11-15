class Solution:
    def exclusiveTime(self, n: int, logs: list[str]) -> list[int]:
        et=[0]*n
        mlogs=[]
        stack=[]
        for each in logs:
            cur=each.split(":")
            mlogs.append(cur)
        for i in range(len(mlogs)):
            # [index,task,time]=logs[i].split(":")
            [index,task,time]=mlogs[i]
            if(task=="start"):
                next=mlogs[i+1]
                et[int(index)]+=int(next[2])-int(time)
                if(i-1>=0):
                    pre=mlogs[i-1]
                    # print("**",pre)
                    if(pre[1]=="end" and stack):
                        print("*",stack,i)
                        et[stack[-1]]+=int(time)-int(pre[2])-1
                # et[int(index)]+=
                if(next[1]=="end"):
                    et[int(index)]+=1
                stack.append(int(index))
            else:
                stack.pop()
                pre=mlogs[i-1]
                if(pre[1]=="end"):
                    et[int(index)]+=int(time)-int(pre[2])
        return et