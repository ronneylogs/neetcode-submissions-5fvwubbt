class LRUCache:

    def __init__(self, capacity: int):
        self.cache = []
        self.cap = capacity
        

    def get(self, key: int) -> int:
        # If it exists
        for i in range(len(self.cache)):
            if self.cache[i][0] == key:
                # Update the value of the key
                item = self.cache.pop(i)
                self.cache.append(item)
                return item[1]
        return -1

    def put(self, key: int, value: int) -> None:
        # If it exists
        for i in range(len(self.cache)):
            if self.cache[i][0] == key:
                # Update the value of the key
                item = self.cache.pop(i)
                item[1] = value
                self.cache.append(item)
                return


        # If it doesn't exist
            # Check if it overloads cap
        if len(self.cache) == self.cap:
            self.cache.pop(0)

            # Add to cache
        self.cache.append([key,value])
        
