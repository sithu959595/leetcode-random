# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if(not root):
            return []
        q=deque([root])
        count=1
        nextC=0
        res=[]
        curArr=[]
        while(count):
            # while(count):
            cur=q.popleft()
            count-=1
            curArr.append(cur.val)
            if(cur.left):
                q.append(cur.left)
                nextC+=1
            if(cur.right):
                q.append(cur.right)
                nextC+=1
            if(not count):
                count=nextC
                nextC=0
                curArr=[]
                res.append(curArr)
        return res