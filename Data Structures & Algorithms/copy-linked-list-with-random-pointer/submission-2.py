class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        mp = {}

        dummy = Node(0)
        cur = dummy
        org = head

        # Create copied nodes + next pointers
        while org:
            new = Node(org.val)

            cur.next = new
            cur = new

            mp[org] = new

            org = org.next

        # Add random pointers
        org = head
        cur = dummy.next

        while org:
            if org.random:
                cur.random = mp[org.random]

            org = org.next
            cur = cur.next

        return dummy.next