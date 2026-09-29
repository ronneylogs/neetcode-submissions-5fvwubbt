class Node:
    def __init__(self, key:int,value:int):
        self.val = value
        self.key = key
        self.next = None
        self.prev = None



class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.left = Node(0,0)
        self.right = Node(0,0)

        self.right.prev = self.left
        self.left.next = self.right

    def remove(self,node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

    def insert(self,node):
        prev = self.right.prev
        nxt = self.right

        prev.next = node
        nxt.prev = node

        node.prev = prev
        node.next = nxt



    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val

        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            self.remove(self.cache[key])
            self.insert(self.cache[key])

        else:
            self.cache[key] = Node(key,value)
            self.insert(self.cache[key])
            if len(self.cache) > self.cap:
                lru = self.left.next
                self.remove(lru)
                del self.cache[lru.key]




# Idea
# 1. left should point to LRU (to remove)
# 2. right should point to MRU (where to add next)


# Two data structures:
# - cache {}: for easy lookup to see if a value exists in our cache O(1)
# - LL: for easy insertion O(1), 

# Node should have:
# - value
# - next
# - prev

# cache should have:
# {key:node}


