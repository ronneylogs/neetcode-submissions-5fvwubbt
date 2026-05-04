class Node:
    def __init__(self,k:int,v:int):
        self.key = k
        self.val = v

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


    def insert(self,node):
        orig = self.right.prev
        orig.next = node
        node.next = self.right
        node.prev = orig
        self.right.prev = node

    
    def remove(self,node):
        prev = node.prev
        prev.next = node.next
        
        nxt = node.next
        node.next.prev = prev
        



        return

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            self.cache[key] = Node(key,value)
            self.insert(self.cache[key])
            
        else:
            self.cache[key] = Node(key,value)
            self.insert(self.cache[key])
            
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


        


    # we use a hashmap to find values faster
        # key: the key number
        # value: Node itself

    # have two dummy nodes, lru and mru
        # structure should be doubly linked list
    