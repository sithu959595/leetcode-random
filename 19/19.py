# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l=0
        h=head
        while(h):
            l+=1
            h=h.next
        cur=ListNode(None,head)
        tem=cur
        target=l-n+2
        p=0
        pre=None
        while(True):
            p+=1
            if(p==target):
                pre.next=cur.next
                cur.next=None
                return tem.next
            pre=cur
            cur=cur.next