# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head == None or head.next==None:
            return
        
        remove = head
        ahead = head

        gap = 0
        while gap !=n:
            ahead = ahead.next
            gap +=1

        if ahead == None:
            return head.next
        
        while ahead and ahead.next!=None:
            remove = remove.next
            ahead = ahead.next
        
        remove.next = remove.next.next

        
        return head

        

    
    # Idea
    # two pointers:one at the beginning, another one that is n away
    # when the n away pointer next pointer reaches null, we remove the first pointer,