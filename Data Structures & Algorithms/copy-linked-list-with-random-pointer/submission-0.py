"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None
        cur = head.next
        newCur = Node(head.val)
        copied = newCur
        
        # create the nodes
        while cur:
            nextNode = Node(cur.val)
            newCur.next = nextNode
            cur = cur.next
            newCur = newCur.next


        nodeMap = dict()

        cur = head
        new = copied
        
        # map old to new
        while cur and new:
            nodeMap[cur] = new
            cur = cur.next
            new = new.next


        cur = head
        new = copied

        # copy over random pointers
        while cur:
            if cur.random:
                new.random = nodeMap[cur.random]

            cur = cur.next
            new = new.next
    
        return copied

        


        # {address of original node, address of copied node}

        # idea: create the copies first, fill in val and next
        # go back again and map the address of original to address of copied node
        # go through again to map the random pointers