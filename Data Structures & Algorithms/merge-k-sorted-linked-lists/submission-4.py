# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class NodeWrapper:
    def __init__(self,node):
        self.node = node
    
    def __lt__(self,other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for i in range(len(lists)):
            if lists[i] is not None:
                heap.append(NodeWrapper(lists[i]))

        heapq.heapify(heap)

        dummy = ListNode()
        cur = dummy
        while heap:
            item = heapq.heappop(heap)
            nxt = item.node.next
            if nxt is not None:
                heapq.heappush(heap,NodeWrapper(nxt))
            
            cur.next = (item.node)
            cur = cur.next

        return dummy.next







# add all of the heads of each LL to the heap
# consistently take the smallest each time, then increment that LL