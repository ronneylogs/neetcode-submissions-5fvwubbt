class LRUCache:

    def __init__(self, capacity: int):
        self.cache = []
        self.cap = capacity
        

    def get(self, key: int) -> int:
        # for loop to find item in cache
        for i in range(len(self.cache)):
            # if found we remove from the cache and append it to the end of list
            if self.cache[i][0] == key:
                item = self.cache.pop(i)
                self.cache.append(item)
                # return
                return self.cache[-1][1]
        
        return -1
        
        

    def put(self, key: int, value: int) -> None:
        # for loop to find item in cache
        for i in range(len(self.cache)):
            # if found we remove from the cache and append it to the end of list
            if self.cache[i][0] == key:
                self.cache.pop(i)
                self.cache.append([key,value])
                # return
                return
        
        # if not found then, make space for it
        if len(self.cache) == self.cap:
            self.cache.pop(0)

        # add to cache
        self.cache.append([key,value])
