# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = list1
        cur2 = list2

        dummy = ListNode(0)
        ret = dummy

        while cur1 and cur2:
            if cur1.val > cur2.val:
                dummy.next = ListNode(cur2.val)
                dummy = dummy.next
                cur2 = cur2.next
            else:
                dummy.next = ListNode(cur1.val)
                dummy = dummy.next
                cur1 = cur1.next

        if cur1:
            dummy.next = cur1
        else:
            dummy.next = cur2

        return ret.next


        