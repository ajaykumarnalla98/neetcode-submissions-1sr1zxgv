class MinStack:

    def __init__(self):
        self.minStack = []

    def push(self, val: int) -> None:
        self.minStack.append(val)

    def pop(self) -> None:
        self.minStack.pop()

    def top(self) -> int:
        return self.minStack[-1]

    def getMin(self) -> int:
        tmp = []
        mini = self.minStack[-1]

        while len(self.minStack):
            mini = min(mini, self.minStack[-1])
            tmp.append(self.minStack.pop())

        while len(tmp):
            self.minStack.append(tmp.pop())
        
        return mini
    