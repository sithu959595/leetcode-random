# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temHead=head
        if(not head or not k):
            return head
        if(not head.next):
            return head
        def recur(cur,count):
            nonlocal head
            count+=1
            if(cur.next==None):
                if(k%count==0):
                    return [float('inf'),float('-inf'),None]
                cur.next=head
                return [1,k%count,cur]
            n=recur(cur.next,count)
            if(n[0]==n[1]):
                # print(cur.val,n[1])
                head=cur.next
                cur.next=None
            return [n[0]+1,n[1],n[2]]
        recur(head,0)
        return head