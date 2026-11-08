# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
        res=0
        def dfs(cur,n):
            nonlocal res
            nn=(n*10)+cur.val
            if(not cur.left and not cur.right):
                res+=nn
                return
            if(cur.left):
                dfs(cur.left,nn)
            if(cur.right):
                dfs(cur.right,nn)

        dfs(root,0)
        return res

sol=Solution()
