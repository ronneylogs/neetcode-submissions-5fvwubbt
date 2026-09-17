# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        prev = dummy
        ahead = dummy

        # Move ahead n nodes forward
        for _ in range(n):
            ahead = ahead.next

        print(ahead.val)

        # Move both until ahead reaches the last node
        while ahead.next:
            prev = prev.next
            ahead = ahead.next

        # prev is now one node before the node we want to remove
        prev.next = prev.next.next

        return dummy.next
        
        



        # we have two pointers, one is n nodes in front of the other. Both increment

        # as soon as n+1 is null, we make the first one point to it's skip

        # edge cases:
        # 1. [], return None
        # 2. [1], one item. return None
        # 3. [1,2], and n=2 return second item
        