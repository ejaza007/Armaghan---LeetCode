class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minstack or val <= self.minstack[-1]:
            self.minstack.append(val)

    def pop(self) -> None:
        if self.stack:
            val = self.stack.pop()
            if val == self.minstack[-1]:
                self.minstack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            raise IndexError("Stack is empty")

    def getMin(self) -> int:
        if self.minstack:
            return self.minstack[-1]
        else:
            raise IndexError("Min stack is empty")
