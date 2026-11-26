class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # prerequisites.sort(key=lambda x:x[1])
        if(not prerequisites):
            return True
        pre={}
        for each in prerequisites:
            if(each[1] not in pre):
                pre[each[1]]=[]
            pre[each[1]].append(each[0])
            print("*",pre)
        order=[]
        visited=set()
        same=set()
        def dfs(cur):
            print(cur,pre)
            nxt=pre[cur] if cur in pre else []
            visited.add(cur)
            # same.add(cur)
            r=True
            for n in nxt:
                if(n in same):
                    return False
                if(n not in visited):
                    same.add(n)
                    r=r and dfs(n)
                    same.remove(n)
            return r
        # print(prerequisites[0][1])
        # res=dfs(prerequisites[0][1])
        # return res
        for i in range(numCourses):
            res=True
            if(i not in visited):
                same.add(i)
                res= dfs(i)
                same.remove(i)
            if(not res):
                return res
        return True