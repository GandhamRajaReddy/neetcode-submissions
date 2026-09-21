# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr=head
        nodes=[]
        while curr:
            nodes.append(curr)
            curr=curr.next
        removeindex=len(nodes)-n    
        if nodes[removeindex]==head:
            return head.next
        nodes[removeindex-1].next=nodes[removeindex].next
        return head    


            
            

        