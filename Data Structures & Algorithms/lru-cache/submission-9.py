

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.cap = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        item = self.cache[key]
        self.cache.move_to_end(key) 
        return item 
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.cap:
            self.cache.popitem(0)

        


# idea: use an ordered list, so we can keep track of most recently used
# when using a key, mark it recently by moving it to the end of the order
# when cache exceeds capacity, remove key at the front of the order