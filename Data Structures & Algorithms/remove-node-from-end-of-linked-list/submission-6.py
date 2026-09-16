# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head == None or head.next == None:
            return None

        orig = head
        sec = head
        cur = head
        counter = 0
        while sec and counter != n:
            sec = sec.next
            counter +=1
        
        while sec and sec.next:
            orig = orig.next
            sec = sec.next


        if sec==None:
            return head.next

        orig.next = orig.next.next
            
        return head
        
        



        # we have two pointers, one is n nodes in front of the other. Both increment

        # as soon as n+1 is null, we make the first one point to it's skip

        # edge cases:
        # 1. [], return None
        # 2. [1], one item. return None
        # 3. [1,2], and n=2 return second item
        