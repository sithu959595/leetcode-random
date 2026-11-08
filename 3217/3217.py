# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        s=set()
        for each in nums:
            s.add(each)
        start=ListNode(None,head)
        cur=start
        while(cur.next):
            if(cur.next.val in s):
                cur.next=cur.next.next
            else:
                cur=cur.next
        return start.next