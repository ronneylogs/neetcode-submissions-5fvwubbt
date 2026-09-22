class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0 

        dummy = ListNode(0)
        new = dummy

        while l1 or l2:

            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            summ = val1 + val2 + carry

            place = summ % 10
            carry = summ // 10

            node = ListNode(place)
            new.next = node
            new = new.next

            if l1:
                l1 = l1.next
            
            if l2:
                l2 = l2.next

        if carry:
            new.next = ListNode(carry)

        return dummy.next