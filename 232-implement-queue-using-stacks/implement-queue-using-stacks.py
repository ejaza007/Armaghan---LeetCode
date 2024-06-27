class MyQueue:

    def __init__(self):
        self.stack = []
        self.reversestack = []

    def push(self, x: int) -> None:
        # Always push to the main stack
        self.stack.append(x)

    def pop(self) -> int:
        # If the reverse stack is empty, transfer all elements from the main stack
        if not self.reversestack:
            while self.stack:
                self.reversestack.append(self.stack.pop())
        # Pop the element from the reverse stack
        return self.reversestack.pop()

    def peek(self) -> int:
        # If the reverse stack is empty, transfer all elements from the main stack
        if not self.reversestack:
            while self.stack:
                self.reversestack.append(self.stack.pop())
        # Peek the element from the reverse stack
        return self.reversestack[-1]

    def empty(self) -> bool:
        # Queue is empty if both stacks are empty
        return not self.stack and not self.reversestack

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
