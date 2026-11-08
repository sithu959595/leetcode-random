# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: ListNode | None) -> ListNode | None:
        d={}
        even=set()
        t=head
        gg=1
        cc=0
        while(t):
            cc+=1
            t=t.next
            if(t==None or cc==gg):
                if(cc%2==0):
                    even.add(gg)
                cc=0
                gg+=1
        print(even)
        def recur(cur,count,group):
            oldCount=count
            if(not cur):
                return [cur,None,None]
            if(count==0): # start of a group
                d[group]=cur
            tem=group
            count+=1
            if(count==group or cur.next==None):
                group+=1
                count=0
            [start,mid,end]=recur(cur.next,count,group)
            if(tem in even): #even gorup
                if(count==0): # end of the gorup
                    d[tem].next=start
                    # cur.next=d[tem]
                    return [cur,cur,d[tem]]
                elif(count==1): #start of the group
                    mid.next=end
                    return [start,None,end]
                else:
                    mid.next=cur
                    return [start,cur,end]
            else: #odd group
                if(count==0): #end of the group
                    cur.next=start
                    return [cur,None,None]
                else:
                    return [cur,None,None]
        recur(head,0,1)
        return head