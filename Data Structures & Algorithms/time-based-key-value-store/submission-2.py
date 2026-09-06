class TimeMap:

    def __init__(self):
        self.keyStore = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        
        self.keyStore[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keyStore:
            return ""

        l = 0 
        r = len(self.keyStore[key]) - 1
        res = ""

        while l <= r:
            m = (l+r) // 2

            if self.keyStore[key][m][0] <= timestamp:
                res = self.keyStore[key][m][1]
                l = m+1
            else:
                r = m - 1
        
        return res






        # seen = -1
        # for t in self.keyStore[key]:
        #     if t <= timestamp:
        #         seen = max(seen,t)
        
        # return "" if seen == -1 else self.keyStore[key][seen]

        


