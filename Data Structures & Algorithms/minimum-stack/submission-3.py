class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        item = self.stack[-1]
        return item
        

    def getMin(self) -> int:
        small = min(self.stack)
        return small
        
