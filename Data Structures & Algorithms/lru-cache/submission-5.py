class LRUCache:

    def __init__(self, capacity: int):
        self.cache = []
        self.cap = capacity
        

    def get(self, key: int) -> int:
        # in cache
        for i in range(len(self.cache)):
            if self.cache[i][0] == key:
                item = self.cache.pop(i)
                self.cache.append(item)
                return item[1]

        return -1

        

    def put(self, key: int, value: int) -> None:

        # in cache
        for i in range(len(self.cache)):
            if self.cache[i][0] == key:
                self.cache.pop(i)
                self.cache.append([key,value])
                return
                # return item[1]
        
        # not in cache
        if len(self.cache) == self.cap:
            self.cache.pop(0)
        
        self.cache.append([key,value])

        
        
