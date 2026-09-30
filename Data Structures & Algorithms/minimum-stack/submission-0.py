class MinStack:

    def __init__(self):
        self.stk = []
        self.currMin = []

    def push(self, val: int) -> None:
        self.stk.append(val)
        if self.currMin == [] or self.currMin[-1]>val:
            self.currMin.append(val)
        else:
            self.currMin.append(self.currMin[-1])

    def pop(self) -> None:
        self.stk.pop()
        self.currMin.pop()
        

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.currMin[-1]
