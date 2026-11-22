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
        cur=head
        target=l-n+1
        p=0
        pre=None
        while(True):
            p+=1
            if(p==target):
                pre=cur.next
                cur.next=None
                return head
            pre=cur
            cur=cur.next