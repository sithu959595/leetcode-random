# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p=ListNode(float("inf"),head)
        h=[]
        def recur(cur):
            if(not cur.next):
                heapq.heappush(h,cur.val)
                return cur
            pre=recur(cur.next)
            if(cur.val>h[-1]): #keep
                cur.next=pre
                return cur
            else: #discar
                cur.next=None
                return pre
        recur(p)
        return p.next