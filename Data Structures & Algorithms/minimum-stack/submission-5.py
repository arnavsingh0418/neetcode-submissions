class MinStack:

    def __init__(self):
        self.stack = []
        self.minS = []
        self.minV = float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minV = min(self.minV, self.stack[-1] if self.stack else self.minV)
        self.minS.append(self.minV if self.minV < val else val)
        
    def pop(self) -> None:
        self.stack.pop()
        self.minS.pop()
        self.minV = self.minS[-1] if self.minS else float('inf')
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minS[-1]
