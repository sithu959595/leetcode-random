class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        rotate=[]
        count=0
        arr=[[skills[i],i] for i in range(len(skills))]
        cur=arr[0]
        for i in range(1,len(arr)):
            if(cur[0]<arr[i][0]):
                rotate.append(cur)
                cur=arr[i]
                count=1
            else:   #win
                count+=1
                if(count==k):
                    return cur[1]
                rotate.append(arr[i])
        return cur[1]