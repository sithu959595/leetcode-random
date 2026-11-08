class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ones=cur=0
        rl=[0 for _ in range(len(boxes))]
        lr=[0 for _ in range(len(boxes))]
        res=[0 for _ in range(len(boxes))]
        for i in range(len(boxes)-1,-1,-1):
            # print(i,cur,ones)
            cur+=ones
            rl[i]=cur
            # cur=rl[i]
            if(boxes[i]=="1"):
                print(i)
                ones+=1
        cur=ones=0
        for j in range(len(boxes)):
            cur+=ones
            lr[j]=cur
            if(boxes[j]=="1"):
                ones+=1
        for k in range(len(boxes)):
            res[k]=rl[k]+lr[k]
        return res


sol=Solution()
boxes = "001011"
boxes = "110"
sol.minOperations(boxes)
