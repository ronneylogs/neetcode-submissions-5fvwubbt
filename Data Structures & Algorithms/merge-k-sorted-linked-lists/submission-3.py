# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        

        while len(lists) > 1:
            temp = []
            for i in range(0,len(lists),2):
                list1 = lists[i]
                list2 = lists[i+1] if len(lists) > i+1 else None

                temp.append(self.mergeLists(list1,list2))

            lists = temp
        
        return lists[0]


    def mergeLists(self,l1,l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        dummy = ListNode()
        cur = dummy
        while l2 and l1:
            if l2.val>=l1.val:
                cur.next = l1
                cur = cur.next
                l1 = l1.next
            else:
                cur.next = l2
                cur = cur.next
                l2 = l2.next
            
        if l1:
            cur.next = l1
        
        if l2:
            cur.next = l2
        
        return dummy.next














        # idea
        # merge two lists each time throughout outer lists
            # do it again for the remaining lists unitl empty, think pyramid
        