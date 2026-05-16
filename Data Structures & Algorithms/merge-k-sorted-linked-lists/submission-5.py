# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for i,n in enumerate(lists):
            if n:
                heapq.heappush(heap,(n.val,i,n))


        dummy = ListNode(0)
        cur = dummy

        while heap:
            node = heapq.heappop(heap)
            cur.next = node[2]
            cur = cur.next
            
            if node[2].next:
                heapq.heappush(heap,(node[2].next.val,node[1],node[2].next))
        

        return dummy.next
        # idea: initialize a heap
            # add first item of each list to the heap, rank by value, list number, and node address
        # instantiate dummy node
        # while the heap exists
        #     pop each node
        #     if the next node exists, add it to the heap
        #     cycle to the next node in the LL